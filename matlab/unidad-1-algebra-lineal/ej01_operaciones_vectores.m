% ej01_operaciones_vectores
% Unidad I: Algebra Lineal y Geometria Diferencial
% Objetivo: repasar producto punto, norma, angulo entre vectores y producto matricial.
% Fecha: 2026-09

clear; clc;

u = [3; 4];
v = [1; 0];

fprintf('u = [%g %g]\n', u);
fprintf('v = [%g %g]\n', v);
fprintf('producto punto : %.4f\n', dot(u, v));
fprintf('norma de u     : %.4f\n', norm(u));

cosTheta = dot(u, v) / (norm(u) * norm(v));
fprintf('angulo u-v     : %.2f grados\n', rad2deg(acos(min(max(cosTheta, -1), 1))));

A = [2 1; 1 3];
disp('A ='); disp(A);
disp('A*u ='); disp(A * u);
fprintf('det(A) = %.4f\n', det(A));

[vectores, valores] = eig(A);
disp('valores propios ='); disp(diag(valores).');
disp('vectores propios ='); disp(vectores);
