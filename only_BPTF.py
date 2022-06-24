import numpy as np
import matlab
import matlab.engine
import scipy.io as sio

# Change path to where export_BPTF is saved
# import sys
# positionOfPath = 1
    # File location
# r = "C:/Users/ncbrubaker/Documents/export_bptf"
# sys.path.insert( positionOfPath, r)

# Run .m file
eng = matlab.engine.start_matlab()
# eng.demo(nargout=0)

# Set Variables in Python
tte = 'TTe.mat';
ttr = 'TTr.mat';
D = 30;
alpha = 2;

hyper_param= {};
hyper_param["Walpha"] = alpha;
hyper_param["nuAlpha"] = 1;

pn = 50e-3;
max_iter = 300;
learn_rate = 1e-3;
n_sample = 50;
range = matlab.double([1, 5])

rates = {};
rates["ridge"] = pn;
rates["learn_rate"] = learn_rate;
rates["range"] = range;
rates["max_iter"] = max_iter;

samples = {};
samples["max_iter"] = n_sample;
samples["n_sample"] = n_sample;
samples["save_sample"] = False;
samples["run_name"] = 'alpha2-1';

# [U, V, dummy, r_pmf] = PMF_Grad(CTr, CTe, D, ...
#    struct('ridge',pn,'learn_rate',learn_rate,'range',[1,5],'max_iter',max_iter));
# fprintf('PMF: %.4f\n', r_pmf);

#[Us_bptf Vs_bptf Ts_bptf] = BPTF(TTr, TTe, D, struct('Walpha',alpha, 'nuAlpha',1), ...
#    {U,V,ones(D,TTr.size(3))}, struct('max_iter',n_sample,'n_sample',n_sample,'save_sample',false,'run_name','alpha2-1'));

bptf = eng.call_BPTF(ttr, tte, D, hyper_param, rates, samples, nargout=4)
print(bptf)

# a = eng.workspace['a'] # get the variable 'a' from the workspace
# print(a)

print("Hello!")

eng.quit()
