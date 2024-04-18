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
    room = settingsdata['core']['room']

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
    useWew = settingsdata['functionSettings']['useWew']
    usePing = settingsdata['functionSettings']['usePing']
    useRaiseLevel = settingsdata['functionSettings']['useRaiseLevel']
    useAlert = settingsdata['functionSettings']['useAlert']
    useDice = settingsdata['functionSettings']['useDice']
    useVend = settingsdata['functionSettings']['useVend']
    translateURLs = settingsdata['functionSettings']['translateURLs']
    useDeletion = settingsdata['functionSettings']['useDeletion']
    useBan = settingsdata['functionSettings']['useBan']
    usePrestige = settingsdata['functionSettings']['usePrestige']
    useModerationTools = settingsdata['functionSettings']['useModerationTools']


class ucalLevels:
    Help = settingsdata['ucalLevels']['Help']
    Filsay = settingsdata['ucalLevels']['Filesay']
    ReadDate = settingsdata['ucalLevels']['ReadDate']
    Timez = settingsdata['ucalLevels']['Timez']
    ucal = settingsdata['ucalLevels']['UCAL']
    GetLike = settingsdata['ucalLevels']['GetLike']
    GetHate = settingsdata['ucalLevels']['GetHate']
    ReadLike = settingsdata['ucalLevels']['ReadLike']
    ReadHate = settingsdata['ucalLevels']['ReadHate']
    Backlog = settingsdata['ucalLevels']['Backlog']
    AutoBacklog = settingsdata['ucalLevels']['AutoBacklog']
    Urbandict = settingsdata['ucalLevels']['Urbandict']
    Translations = settingsdata['ucalLevels']['Translations']
    Vote = settingsdata['ucalLevels']['Vote']
    Issues = settingsdata['ucalLevels']['Issues']
    Rules = settingsdata['ucalLevels']['Rules']
    SRule = settingsdata['ucalLevels']['SRule']
    MiniMods = settingsdata['ucalLevels']['MiniMods']
    RegUsers = settingsdata['ucalLevels']['RegUsers']
    Wheelie = settingsdata['ucalLevels']['Wheelie']
    Fight = settingsdata['ucalLevels']['Fight']
    CMessages = settingsdata['ucalLevels']['CMessages']
    Jokes = settingsdata['ucalLevels']['Jokes']
    Cuss = settingsdata['ucalLevels']['Cuss']
    Insults = settingsdata['ucalLevels']['Insults']
    Drink = settingsdata['ucalLevels']['Drink']
    Wew = settingsdata['ucalLevels']['Wew']
    Ping = settingsdata['ucalLevels']['Ping']
    raiseLevel = settingsdata['ucalLevels']['raiseLevel']
    alert = settingsdata['ucalLevels']['alert']
    dice = settingsdata['ucalLevels']['dice']
    vend = settingsdata['ucalLevels']['vend']
    ban = settingsdata['ucalLevels']['ban']

class keys:
    deeplKey = settingsdata['keys']['DeeplKey']


class moderation:
    minimods = settingsdata['moderation']['miniMods']
    triggers = settingsdata['moderation']['triggers']
