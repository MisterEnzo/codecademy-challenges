# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}
def convert_damages(list):
  converted_list =[]
  for i, v in enumerate(list):
    if "M" in v:
      converted_list.append(float(v.replace("M", ""))*conversion["M"])
    elif "B" in v:
      converted_list.append(float(v.replace("B", ""))*conversion["B"])
    else:
      converted_list.append(v)
  return converted_list



# test function by updating damages
converted_damages = convert_damages(damages)
# print(converted_damages)

# 2 
# Create a Table
def create_table(names, months, years, max_sus_wind, areas, damages, deaths):
  table = {}
  for (n, mo, yr, wind, a, dmg, d) in zip(names,months, years, max_sus_wind, areas, damages, deaths):
    table[n] = {"Name": n, "Month": mo, "Year": yr, "Max Sustained Wind": wind, "Areas Affected": a, "Damage": dmg, "Deaths": d}
  return table
# Create and view the hurricanes dictionary
data = create_table(names, months, years, max_sustained_winds, areas_affected, converted_damages, deaths)
# print(data)
# 3
# Organizing by Year
def organize_by_year(dict):
  organized_by_year = {}
  for k,v in dict.items():
    if v["Year"] in organized_by_year:
      organized_by_year[v["Year"]].append(v)
    else:
      organized_by_year[v["Year"]] = [v]
  return organized_by_year
# create a new dictionary of hurricanes with year and key
# yearly_data = organize_by_year(data)
# print(yearly_data[1932])
# print(yearly_data)
# 4
# Counting Damaged Areas

# create dictionary of areas to store the number of hurricanes involved in


# 5 
# Calculating Maximum Hurricane Count
def max_hur_count(dict):
  max_hur_count = {}
  for k, v in data.items():
    for area in v["Areas Affected"]:
      if area in max_hur_count:
        max_hur_count[area] += 1
      else:
        max_hur_count[area] = 1
  return max_hur_count
max_hur_count = max_hur_count(data)
print(max_hur_count)

# find most frequently affected area and the number of hurricanes involved in
def most_hit(dict):
  hits = 0
  most_hit = []
  for k, v in dict.items():
    if v > hits:
      hits = v
      most_hit = [k]
    elif v == hits:
      most_hit.append(k)
  return hits, most_hit
hits, most_hit = most_hit(max_hur_count)
print(hits)
print(most_hit)

# 6
# Calculating the Deadliest Hurricane
def most_deadly(dict):
  deaths = 0
  most_deaths = []
  for k, v in dict.items():
    if v["Deaths"] > deaths:
      deaths = v["Deaths"]
      most_deaths = [k]
    elif v["Deaths"] == deaths:
      most_deaths.append(k)
  return deaths, most_deaths
deaths, most_deaths = most_deadly(data)


# find highest mortality hurricane and the number of deaths
# print(deaths)
# print(most_deaths)
# 7
# Rating Hurricanes by Mortality
mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}
def mortality_rating(data):
  m_rating = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
  for k, v in data.items():
    if v["Deaths"] == mortality_scale[0]:
      m_rating[0].append(k)
    elif v["Deaths"] > mortality_scale[0] and v["Deaths"] <= mortality_scale[1]:
      m_rating[1].append(k)
    elif v["Deaths"] > mortality_scale[1] and v["Deaths"] <= mortality_scale[2]:
      m_rating[2].append(k)
    elif v["Deaths"] > mortality_scale[2] and v["Deaths"] <= mortality_scale[3]:
      m_rating[3].append(k)
    elif v["Deaths"] > mortality_scale[3] and v["Deaths"] <= mortality_scale[4]:
      m_rating[4].append(k)
    else:
      m_rating[5].append(k)
  return m_rating


# categorize hurricanes in new dictionary with mortality severity as key
m_rating = mortality_rating(data)
print(m_rating)
# 8 Calculating Hurricane Maximum Damage
def most_dmg(data):
  most_dmg = []
  dmg = 0
  for k, v in data.items():
    if v["Damage"] == "Damages not recorded":
      continue
    elif v["Damage"] == dmg:
      most_dmg.append(k)
    elif v["Damage"] > dmg:
      most_dmg = [k]
      dmg = v["Damage"]
  return most_dmg, dmg

# find highest damage inducing hurricane and its total cost
most_dmg, dmg = most_dmg(data)
print(most_dmg)
print(dmg)

# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  
# categorize hurricanes in new dictionary with damage severity as key
def damage_rating(data):
  d_rating = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], "No Rating":[],}
  for k, v in data.items():
    if v["Damage"] == "Damages not recorded":
      d_rating["No Rating"].append(k)
    elif v["Damage"] == damage_scale[0]:
      d_rating[0].append(k)
    elif v["Damage"] > damage_scale[0] and v["Damage"] <= damage_scale[1]:
      d_rating[1].append(k)
    elif v["Damage"] > damage_scale[1] and v["Damage"] <= damage_scale[2]:
      d_rating[2].append(k)
    elif v["Damage"] > damage_scale[2] and v["Damage"] <= damage_scale[3]:
      d_rating[3].append(k)
    elif v["Damage"] > damage_scale[3] and v["Damage"] <= damage_scale[4]:
      d_rating[4].append(k)
    else:
      d_rating[5].append(k)
  return d_rating
dmg_rating = damage_rating(data)
print(dmg_rating)
