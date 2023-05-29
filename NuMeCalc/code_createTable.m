%CREATETABLE Summary of this function goes here
%   Detailed explanation goes here
function [listTable] = code_createTable(c,err,x1,listTable)
    n=length(x1);
    listTable(c+1,1)=c;
    listTable(c+1,2)=err;
    for index=1:n
        listTable(c+1,2+index)=x1(index);
    end
end