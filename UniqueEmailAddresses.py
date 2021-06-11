class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        new_emails = []
        for email in emails:
            arr = email.split("@")
            domain = arr[1]
            local = arr[0].split("+")[0]
            local = local.replace(".", "")
            new_emails.append("{0}@{1}".format(local, domain))
            
        s = set(new_emails)
        
        return len(s)
