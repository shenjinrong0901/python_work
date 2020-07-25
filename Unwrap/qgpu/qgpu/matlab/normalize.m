% * * * * * * * * * * * * * * * * *
%  Normalize a matrix
%

function [n_map] = normalize(map)

    n_map = zeros(size(map));
    n_map(:,:) = map;

    min1 = min(min(n_map));
    n_map = n_map - min1;
    max1 = max(max(n_map));
    n_map = n_map / max1;
end