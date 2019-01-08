#!/usr/bin/env bash
mvdir(){
    for name in "先天性巨痣" "先天性巨痣（Fish+)" "黑色素瘤" "先天性巨痣恶变" "先天性巨痣LN+" ;do
    mkdir $name
    done
    mv G1* "先天性巨痣" 
    mv G2* "先天性巨痣（Fish+)"
    mv G3* "黑色素瘤"
    mv G4* "先天性巨痣恶变"
    mv G5* "先天性巨痣LN+"
}
export -f mvdir
mvdir


