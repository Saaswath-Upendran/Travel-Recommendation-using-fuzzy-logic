import numpy as np 
class FuzzyVariable:
    def __init__():
        pass
    def _adjust_domain_val(self, x_val):
        return self._domain[np.abs(self._domain-x_val).argmin()]

    def create_fuzzy(cls, name, min, max, res, a, b, c):
        t1fs = cls(name, min, max, res)

        a = t1fs._adjust_domain_val(a)
        b = t1fs._adjust_domain_val(b)
        c = t1fs._adjust_domain_val(c)

        t1fs._dom = np.round(np.maximum(np.minimum((t1fs._domain-a)/(b-a), (c-t1fs._domain)/(c-b)), 0), t1fs._precision)

    
    def union(self, f_set):

		result = FuzzySet(f'({self._name}) union ({f_set._name})', self._domain_min, self._domain_max, self._res)
		result._dom = np.maximum(self._dom, f_set._dom)

		return result
        pass
    def fuzzify(self, val):

	# get dom for each set and store it - 
	# it will be required for each rule
	    for set_name, f_set in self._sets.items():
		    f_set.last_dom_value = f_set[val]


        pass
    def cog_defuzzify(self):
        num = np.sum(np.multiply(self._dom, self._domain))
        den = np.sum(self._dom)

        return num/den






class FuzzyOutputVariable(FuzzyVariable):

    def __init__(self, name, min_val, max_val, res):
        super().__init__(name, min_val, max_val, res)
        self._output_distribution = FuzzySet(name, min_val, max_val, res)

    def add_rule_contribution(self, rule_consequence):
        self._output_distribution = self._output_distribution.union(rule_consequence)

    def get_crisp_output(self):
        return self._output_distribution.cog_defuzzify()



    def evaluate_antecedent(self):
	    return self._set.last_dom_value

def evaluate_consequent(self, activation):
	self._variable.add_rule_contribution(self._set.min_scalar(activation))




    