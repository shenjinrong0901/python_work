lax_coordinates = (33.9245, -118.408056)
city, year, pop, chg, area = ('Beijing', 1949, 300000, 0.99, 10000)
traveler_ids = [('USA', '123'), ('UK', '456'), ('BRA', '789')]
for passport in sorted(traveler_ids):
    print('%s/%s' % passport)

for country, _ in traveler_ids:
    print(country)