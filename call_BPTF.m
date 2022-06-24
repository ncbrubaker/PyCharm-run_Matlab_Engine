function [Us_bptf Vs_bptf Ts_bptf r_bptf] = call_BPTF(R, E, D, hyper_params, pmf_options, options)

cd ./lib
build;
cd ..
addpath ./lib

Tr = load(R).TTr;
Te = load(E).TTe;
TTr = spTensor(Tr.subs, Tr.vals, Tr.size);
TTe = spTensor(Te.subs, Te.vals, Te.size);
CTr = TTr.Reduce(1:2);
CTe = TTe.Reduce(1:2);

[U, V, dummy, r_pmf] = PMF_Grad(CTr, CTe, D, pmf_options);
fprintf('PMF: %.4f\n', r_pmf);

[Us_bptf Vs_bptf Ts_bptf] = BPTF(TTr, TTe, D, hyper_params, {U,V,ones(D,TTr.size(3))}, options);
[Y_bptf] = BPTF_Predict(Us_bptf,Vs_bptf,Ts_bptf,D,TTe,[1 5]);
r_bptf = RMSE(Y_bptf.vals-TTe.vals);
fprintf('BPTF: %.4f\n', r_bptf);

r = [r_pmf r_bptf]