class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        output = []
        products.sort()
        for i in range(len(searchWord)):
            search = searchWord[:i+1]
            searchResult = []
            for j in range(len(products)):
                if products[j].startswith(search):
                    searchResult.append(products[j])
                    
                if len(searchResult) == 3:
                    break
                       
            output.append(searchResult)
                       
        return output
