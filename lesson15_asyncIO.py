
# 协程
# def  consumer():
#   r = ''
#   while True:
#     n = yield r
#     if not n:
#       return
#     print('[CONSUMER] Consuming %s...' % n)
#     with open('file/hello.txt','r') as f:
#       s = f.read()
#       r = s
    


# def produce(c,i):
#   c.send(None)
#   n=0
#   while n < 5:
#     n = n + 1
#     print('[PRODUCER %d] Producing %s...' % (i,n))
#     r = c.send(n)
#     print('[PRODUCER %d] Consumer return: %s' % (i,r))
#   c.close()


# c = consumer()

# produce(c,1)   
# produce(c,2)   
# produce(c,3)   


# 异步IO
import asyncio


async def hello():
  print('Hello world!')
  await asyncio.sleep(1)
  print('Hello again!')


loop = asyncio.get_event_loop()
tasks = [hello(),hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()