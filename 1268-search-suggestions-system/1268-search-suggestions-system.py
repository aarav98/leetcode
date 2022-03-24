"""

"""
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        products.sort()
        result, prefix, start = [], '', 0
        
        for c in searchWord:
            prefix += c
            start = bisect.bisect_left(products, prefix, start)
            result.append([w for w in products[start:start+3] if w.startswith(prefix)])
        return result
            
        