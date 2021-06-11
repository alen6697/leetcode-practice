class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        difference = 1
        for i in range(len(emails)):
            original_arr = emails[i].split("@")
            original_domain = original_arr[1]
            original_local = original_arr[0].split("+")[0]
            original_local = original_local.replace(".", "")
            for j in range(i + 1, len(emails)):
                compared_arr = emails[j].split("@")
                compared_domain = compared_arr[1]
                compared_local = compared_arr[0].split("+")[0]
                compared_local = compared_local.replace(".", "")
                if original_domain != compared_domain or original_local != compared_local:
                    difference = difference + 1
                        
            return difference

s = Solution()
print(s.numUniqueEmails(["fg.r.u.uzj+o.pw@kziczvh.com","r.cyo.g+d.h+b.ja@tgsg.z.com","fg.r.u.uzj+o.f.d@kziczvh.com","r.cyo.g+ng.r.iq@tgsg.z.com","fg.r.u.uzj+lp.k@kziczvh.com","r.cyo.g+n.h.e+n.g@tgsg.z.com","fg.r.u.uzj+k+p.j@kziczvh.com","fg.r.u.uzj+w.y+b@kziczvh.com","r.cyo.g+x+d.c+f.t@tgsg.z.com","r.cyo.g+x+t.y.l.i@tgsg.z.com","r.cyo.g+brxxi@tgsg.z.com","r.cyo.g+z+dr.k.u@tgsg.z.com","r.cyo.g+d+l.c.n+g@tgsg.z.com","fg.r.u.uzj+vq.o@kziczvh.com","fg.r.u.uzj+uzq@kziczvh.com","fg.r.u.uzj+mvz@kziczvh.com","fg.r.u.uzj+taj@kziczvh.com","fg.r.u.uzj+fek@kziczvh.com"]))
