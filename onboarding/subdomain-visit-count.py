class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_count = defaultdict(int)

        for cp_domain in cpdomains:
            visit_count , cpdomain = cp_domain.split(" ")
            visit_count = int(visit_count)

            subdomains = cpdomain.split(".")

            for i in range(len(subdomains)):
                subdomain = ".".join(subdomains[i:])
                domain_count[subdomain] += visit_count

        result = []
        for subdomain, visit_count in domain_count.items():
            result.append(str(visit_count) + " " + subdomain)

        return result
