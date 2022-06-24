function [Us_bptf Vs_bptf Ts_bptf r_bptf] = call_BPTF(TTr, TTe, D, hyper_params, pmf_options, options)

load TTr
load TTe
TTr = spTensor(TTr.subs, TTr.vals, TTr.size);
TTe = spTensor(TTe.subs, TTe.vals, TTe.size);
CTr = TTr.Reduce(1:2);
CTe = TTe.Reduce(1:2);

[U, V, dummy, r_pmf] = PMF_Grad(CTr, CTe, D, pmf_options);
fprintf('PMF: %.4f\n', r_pmf);

[Us_bptf Vs_bptf Ts_bptf] = BPTF(TTr, TTe, D, hyper_params, ...
    {U,V,ones(D,TTr.size(3))}, options);
[Y_bptf] = BPTF_Predict(Us_bptf,Vs_bptf,Ts_bptf,D,TTe,[1 5]);
r_bptf = RMSE(Y_bptf.vals-TTe.vals);
fprintf('BPTF: %.4f\n', r_bptf);

r = [r_pmf r_bptf]