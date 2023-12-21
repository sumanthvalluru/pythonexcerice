function factoril(num){
    if(num == 1){
        return 1;
    }

    return num* factoril(num - 1);
}

console.log(factoril(4))
