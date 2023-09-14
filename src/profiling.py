import pstats

p = pstats.Stats('./result.cprofile')
p.sort_stats('cumulative').print_stats()
