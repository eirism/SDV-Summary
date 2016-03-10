# creates db for SDV-Summary

import sqlite3

database_structure = '''id INTEGER PRIMARY KEY AUTOINCREMENT,
md5 TEXT,
url TEXT,
isMale TEXT,
pantsColor0 INT,
pantsColor1 INT,
pantsColor2 INT,
pantsColor3 INT,
combatLevel INT,
maxHealth INT,
hair INT,
favoriteThing TEXT,
maxItems INT,
skin INT,
friendshipsWilly INT,
friendshipsClint INT,
friendshipsJodi INT,
friendshipsHarvey INT,
friendshipsLeah INT,
friendshipsWizard INT,
friendshipsJas INT,
friendshipsAbigail INT,
friendshipsMaru INT,
friendshipsElliott INT,
friendshipsCaroline INT,
friendshipsPam INT,
friendshipsDwarf INT,
friendshipsShane INT,
friendshipsDemetrius INT,
friendshipsAlex INT,
friendshipsGus INT,
friendshipsVincent INT,
friendshipsSebastian INT,
friendshipsRobin INT,
friendshipsSam INT,
friendshipsLewis INT,
friendshipsMarnie INT,
friendshipsPenny INT,
friendshipsHaley INT,
friendshipsPierre INT,
friendshipsEvelyn INT,
friendshipsLinus INT,
friendshipsGeorge INT,
friendshipsEmily INT,
farmingLevel INT,
statsRocksCrushed INT,
statsDaysPlayed INT,
statsStepsTaken INT,
statsSpecificMonstersKilledFly INT,
statsSpecificMonstersKilledGhost INT,
statsSpecificMonstersKilledBat INT,
statsSpecificMonstersKilledSkeleton INT,
statsSpecificMonstersKilledGrub INT,
statsSpecificMonstersKilledDust_Spirit INT,
statsSpecificMonstersKilledStone_Golem INT,
statsSpecificMonstersKilledFrost_Bat INT,
statsSpecificMonstersKilledDuggy INT,
statsSpecificMonstersKilledRock_Crab INT,
statsSpecificMonstersKilledBig_Slime INT,
statsSpecificMonstersKilledSludge INT,
statsSpecificMonstersKilledFrost_Jelly INT,
statsSpecificMonstersKilledBug INT,
statsSpecificMonstersKilledGreen_Slime INT,
statsSpecificMonstersKilledLava_Crab INT,
statsSlimesKilled INT,
statsPreservesMade INT,
statsGeodesCracked INT,
statsSeedsSown INT,
statsNotesFound INT,
statsMonstersKilled INT,
statsStumpsChopped INT,
statsCropsShipped INT,
statsCowMilkProduced INT,
statsFishCaught INT,
statsPiecesOfTrashRecycled INT,
statsTrufflesFound INT,
statsIridiumFound INT,
statsTimesFished INT,
statsStarLevelCropsShipped INT,
statsCopperFound INT,
statsBarsSmelted INT,
statsBouldersCracked INT,
statsCoinsFound INT,
statsCaveCarrotsFound INT,
statsStoneGathered INT,
statsQuestsCompleted INT,
statsGoatMilkProduced INT,
statsCoalFound INT,
statsIronFound INT,
statsCheeseMade INT,
statsItemsCooked INT,
statsWeedsEliminated INT,
statsTimesUnconscious INT,
statsChickenEggsLayed INT,
statsSheepWoolProduced INT,
statsDiamondsFound INT,
statsRabbitWoolProduced INT,
statsAverageBedtime INT,
statsBeveragesMade INT,
statsOtherPreciousGemsFound INT,
statsDuckEggsLayed INT,
statsItemsCrafted INT,
statsGiftsGiven INT,
statsSticksChopped INT,
statsPrismaticShardsFound INT,
statsDirtHoed INT,
statsGoldFound INT,
statsMysticStonesCrushed INT,
statsItemsShipped INT,
statsGoatCheeseMade INT,
shirt INT,
uniqueIDForThisGame TEXT,
miningLevel INT,
facialHair INT,
money INT,
newEyeColor0 INT,
newEyeColor1 INT,
newEyeColor2 INT,
newEyeColor3 INT,
maxStamina INT,
farmName TEXT,
foragingLevel INT,
fishingLevel INT,
deepestMineLevel INT,
accessory INT,
catPerson TEXT,
totalMoneyEarned BIGINT,
millisecondsPlayed BIGINT,
hairstyleColor0 INT,
hairstyleColor1 INT,
hairstyleColor2 INT,
hairstyleColor3 INT,
name TEXT,
professions0 TEXT,
professions1 TEXT,
professions2 TEXT,
professions3 TEXT,
professions4 TEXT,
professions5 TEXT,
professions6 TEXT,
professions7 TEXT,
professions8 TEXT,
professions9 TEXT,
farm_info TEXT,
farm_image TEXT,
added_time FLOAT'''

with sqlite3.connect("sdv.db") as connection:
	c = connection.cursor()
	c.execute('CREATE TABLE playerinfo('+database_structure+')')
	c.execute('CREATE TABLE errors(time BIGINT, notes TEXT)')
	c.execute('CREATE TABLE todo(task TEXT, ID TEXT)')

