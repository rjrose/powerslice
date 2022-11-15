import powerpool
newPool = powerpool.powerPool(100)
newPool.request(20)
newPool.release(10)
newPool.request(30)
newPool.release(60)
newPool.request(80)