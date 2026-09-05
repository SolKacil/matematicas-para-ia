% ej02_suma_escalar_y_producto
% Modulo 1: Algebra lineal y geometria diferencial
% Objetivo: suma de vectores y de matrices, producto por escalar, los tres
% productos entre vectores (punto, elemento a elemento y externo) y la
% multiplicacion de matrices, escrita a mano y verificada contra el operador *.
%
% Ejecuta el script, cambia los vectores y las matrices, y vuelve a ejecutarlo.
% Compatible con MATLAB y GNU Octave.

clear; clc;

%% 1. Suma de vectores: componente a componente, misma dimension
u = [3; 1];
v = [1; 4];

fprintf('u = [%g %g]\n', u);
fprintf('v = [%g %g]\n', v);
fprintf('u + v = [%g %g]\n', u + v);
fprintf('u - v = [%g %g]\n', u - v);

%% 2. Producto por escalar: estira, encoge o voltea
fprintf('\n2*u    = [%g %g]   norma %.4f\n', 2 * u, norm(2 * u));
fprintf('-1.5*u = [%g %g]   norma %.4f\n', -1.5 * u, norm(-1.5 * u));

% Suma y escalar juntos: un paso de descenso de gradiente.
pesos = [1; -2; 0.5];
grad  = [0.4; 0.1; -0.3];
tasa  = 0.1;
fprintf('\npesos - tasa*gradiente = [%g %g %g]\n', pesos - tasa * grad);

%% 3. Los tres productos entre vectores
% OJO: en MATLAB la convencion es al reves que en NumPy.
%   *  es el producto matricial   (a'*b da el producto punto)
%   .* es el elemento a elemento
a = [1; 2; 3];
b = [4; 0; -1];

fprintf('\nproducto punto      : %g   (un escalar)\n', dot(a, b));   % = a'*b
fprintf('elemento a elemento : [%g %g %g]\n', a .* b);
disp('producto externo a*b'' ='); disp(a * b');                      % matriz 3x3

%% 4. Suma de matrices: misma forma, elemento a elemento
A = [1 2; 3 4; 5 6];
B = [10 20; 30 40; 50 60];

disp('A + B ='); disp(A + B);

% Sumar un vector a todas las filas (asi se aplica el sesgo a un lote).
% MATLAB y Octave recientes lo hacen solos; con bsxfun funciona en cualquier version.
lote  = [1 2 3; 4 5 6; 7 8 9];
sesgo = [100 200 300];
disp('lote + sesgo ='); disp(bsxfun(@plus, lote, sesgo));

%% 5. Matriz por escalar
disp('3 * A ='); disp(3 * A);

%% 6. Multiplicacion de matrices: (n x m)(m x p) = (n x p)
M = [1 2 3; 4 5 6];        % 2x3
N = [7 8; 9 10; 11 12];    % 3x2

fprintf('\nM es %dx%d, N es %dx%d -> M*N es %dx%d\n', ...
        size(M), size(N), size(M * N));

% A mano, con la definicion c(i,j) = suma_k a(i,k)*b(k,j)
C = zeros(size(M, 1), size(N, 2));
for i = 1:size(M, 1)
    for j = 1:size(N, 2)
        for k = 1:size(M, 2)
            C(i, j) = C(i, j) + M(i, k) * N(k, j);
        end
    end
end

disp('a mano ='); disp(C);
disp('MATLAB ='); disp(M * N);
fprintf('iguales: %d\n', all(all(abs(C - M * N) < 1e-12)));

% El orden importa: AB no es BA.
R = [0 -1; 1 0];    % rotacion de 90 grados
S = [3 0; 0 1];     % estirar 3x en horizontal
disp('R*S ='); disp(R * S);
disp('S*R ='); disp(S * R);
fprintf('son iguales? %d\n', isequal(R * S, S * R));

%% 7. Todo junto: una capa densa Y = X*W + b
X = [0.5 2.0 -1.0; 1.0 0.0 3.0; -2.0 1.5 0.5; 0.0 -1.0 1.0];  % 4 muestras x 3 rasgos
W = [0.8 -0.5; -0.2 1.1; 1.4 0.3];                            % 3 entradas -> 2 neuronas
sesgoCapa = [0.1 -0.2];

Z = bsxfun(@plus, X * W, sesgoCapa);
salida = max(0, Z);                    % ReLU, elemento a elemento

fprintf('\nX es %dx%d, W es %dx%d -> salida %dx%d\n', ...
        size(X), size(W), size(salida));
disp('salida ='); disp(salida);
