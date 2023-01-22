import YahooFetcher
import ComponentsExtractor

c = ComponentsExtractor.ComponentsExtractor()
#ex = c.getExchange("mse")
ex = c.getExchange("nasdaq")
for e in ex:
  print (e)
