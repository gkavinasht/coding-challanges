# 811. Subdomain Visit Count
# A website domain "discuss.leetcode.com" consists of various subdomains. At the top level, we have "com", at the next level, we have "leetcode.com" and at the lowest level, "discuss.leetcode.com". When we visit a domain like "discuss.leetcode.com", we will also visit the parent domains "leetcode.com" and "com" implicitly.
# A count-paired domain is a domain that has one of the two formats "rep d1.d2.d3" or "rep d1.d2" where rep is the number of visits to the domain and d1.d2.d3 is the domain itself.
# For example, "9001 discuss.leetcode.com" is a count-paired domain that indicates that discuss.leetcode.com was visited 9001 times.
# Given an array of count-paired domains cpdomains, return an array of the count-paired domains of each subdomain in the input. You may return the answer in any order.

import collections
def subdomainVisits(cpdomains):
    domainsCount = collections.defaultdict(int)
    counts = []

    for cpdomain in cpdomains:
        count, domain = cpdomain.split(" ")
        while "." in domain:
            domainsCount[domain] = domainsCount.get(domain, 0) + int(count)
            domain = domain.split(".", 1)[1]
        domainsCount[domain] = domainsCount.get(domain, 0) + int(count)

    for domain, count in domainsCount.items():
        counts.append(f"{count} {domain}")
    return counts

cpdomains = ["9001 discuss.leetcode.com"]
print(subdomainVisits(cpdomains))

# Output: ["9001 leetcode.com","9001 discuss.leetcode.com","9001 com"]
# Explanation: We only have one website domain: "discuss.leetcode.com".
# As discussed above, the subdomain "leetcode.com" and "com" will also be visited. So they will all be visited 9001 times.

# Time Complexity: O(n)
# Space Complexity: O(n)