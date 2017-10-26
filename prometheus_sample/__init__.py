
import pygics
import prometheus
import proc

flow = prometheus.Flow()

gen = proc.TickGenerator()
lgr = proc.Logger()
prt = proc.Printer()

flow.setGenerator(gen)
flow.addProcessor(lgr)
flow.addProcessor(prt)

f1 = prometheus.Filter(mapping={'data' : 'SRC["message"]'})
f2 = prometheus.Filter(mapping={'data' : 'SRC["data"]'})

flow.addInterface(src=gen.getUUID(), dst=lgr.getUUID(), **f1)
flow.addInterface(src=lgr.getUUID(), dst=prt.getUUID(), **f2)

flow.start()

gen.create()
