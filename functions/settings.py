import json

# !!!IMPORTANT!!! if you are just browsing these files, this is not the settintgs file, that is settings.json







# the overarching settings file
with open("json-files/settings.json", "r") as f:
    settingsdata = json.load(f)


class core:
    username = settingsdata['core']['username']
    password = settingsdata['core']['password']
    entrances = settingsdata['core']['entrances']
    name = settingsdata['core']['name']
    version = settingsdata['core']['version']
    trustedUsers = settingsdata['core']['trustedUsers']


class miscSettings:
    logchat = settingsdata['functionSettings']['LogChat']


class funcSettings:
    useHelp = settingsdata['functionSettings']['useHelp']
    useFilsay = settingsdata['functionSettings']['useFilesay']
    useReadDate = settingsdata['functionSettings']['useReadDate']
    useTimez = settingsdata['functionSettings']['useTimez']
    useUCAL = settingsdata['functionSettings']['useUCAL']
    useGetLike = settingsdata['functionSettings']['useGetLike']
    useGetHate = settingsdata['functionSettings']['useGetHate']
    useReadLike = settingsdata['functionSettings']['useReadLike']
    useReadHate = settingsdata['functionSettings']['useReadHate']
    useBacklog = settingsdata['functionSettings']['useBacklog']
    useAutoBacklog = settingsdata['functionSettings']['useAutoBacklog']
    useUrbandict = settingsdata['functionSettings']['useUrbandict']
    useTranslations = settingsdata['functionSettings']['useTranslations']
    useVote = settingsdata['functionSettings']['useVote']
    useIssues = settingsdata['functionSettings']['useIssues']
    useRules = settingsdata['functionSettings']['useRules']
    useSRule = settingsdata['functionSettings']['useSRule']
    useMiniMods = settingsdata['functionSettings']['useMiniMods']
    useRegUsers = settingsdata['functionSettings']['useRegUsers']
    useWheelie = settingsdata['functionSettings']['useWheelie']
    useFight = settingsdata['functionSettings']['useFight']
    useZSH = settingsdata['functionSettings']['useZSH']
    useCMessages = settingsdata['functionSettings']['useCMessages']
    useJokes = settingsdata['functionSettings']['useJokes']
    useCuss = settingsdata['functionSettings']['useCuss']
    useInsults = settingsdata['functionSettings']['useInsults']
    useDrink = settingsdata['functionSettings']['useDrink']


class keys:
    deeplKey = settingsdata['keys']['DeeplKey']


class moderation:
    minimods = settingsdata['moderation']['miniMods']
    useBlacklist = settingsdata['moderation']['useBlacklist']
