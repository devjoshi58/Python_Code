from collections import defaultdict

l = [1,2,2,2,3,1,1]
#l = [1,1,1,1,1,1]
#l = [4,5,6,7,8]
s="""869848510595747964775587604968564451302563059745432980663251117772003451786772415736912240371148571818196986127912514930997203170262293991505417960585574206534872091500653324233281838470123720940090378812237785880927951524518740097870214994692686502654206102101000141732112590140307038660090390326699922371515667360348347579723393407637788464223457512461544993443108806863505872525964140539073504316112483162644132566711730083634257716232418824200174267578831288950595036030452560916865841289096275798393648817020906492532631280759711075158080072813076432780875978095703521728021340086264263950880572055329322586587323969356356534839571406854734466962019847500903852913720195554142563749691681168480954993740184550846706964203163350769236266611818498207727255580558774310174475246166051976447422212643973312048775572662508260681077684136332409986344514432622029709412278410328155736392554758959892319170302230923554909577464573906933165600692177567626583952464057395058037266935819579084230858517214047065688169238157792079820774378076764593426332213411315682010039605175619262683026387847160365427054718664043667295281117443988905599375081548487005328182673485045992690766515515269177547805421131392699260713349479425115878283535794822816360519471984481421877376950164990163000290661023321070965101593819112253449544996204210922304685718136500656065785328321853233924940590775382972605557832377689003074052682091261736632061720722239954315534662957720946328511756641375848426932616920554405771567697393238041232025170733320676565216632446781093723998243520188920585741642763335646691943273086266053317713048724483587007425071697120821325109648916918670377568473485619359315128932719959907746004568503654488272443658540426027705577832472429685241215579384274821726286428418133256024964381965047767329362185623345941392618114002755803323806330146498659562183670181615015651865505572441679137467538039714892665314570647873519284207180860228750137193173444583023943040264042275296526862511013339933950576703424196902156259802997502562354826357947452289180491142610047439084798734974994153288649864609527226092689090425074830747307470392023481513675174570874524473605827187540000717297274846285758252991965967950979618292033618635854140838554663725664060341304919523819666042426102700765895508461042120737199729191177679421297393726091722694705014002944063024316117209680052886286470198412154787738696924102720599500662879477440222014456640809771838247104840163396931528508705801825857432560819603077837829321635110956302304396894597471623796327315965408837438087926088487210263760422405368178062693751474610288450612151180198377642710373414459712947276287124889380319871228390606334152886375405658756880911971536142452001763420396104197205370296633853039393425235646386043264929205820969324847524172908424936889561559703109873481791765259059915382455865973313605981428523446197452951650183746256398172618337093408785703379994546573736689580850929421058149815662955514794799884956071887980446633317786455356761568868577511397958648285943539896674752423785670434475069324203093588722210789944691390244666295543517951259143624955999588207771324239356471055461062910750659983327562109406273571784880045045397063306468385632733311337833395391643410340804397620983869228759036487633615264148136725869656751311294568084629534328004981787930060718548100276730733453521435561734508531668251247582944280956041711776052979214192308047044669932239834343297808148164068545630855839463814795521567965819594789384243746215960016914416387957887422726368156378161502350147046880282838865512520602039065979770890293382853308388881700399478477696026433765513591973923062839598313256552123685074386684067939082308985317897394732510028733832164174607597346921273497570876284992374335080874013583252439080771929574172361985233778133363332425572902350740493762705231684848508010476460609198380003283897969763722388640759587799030339325494796945909985055736951915867509980694117207914509315508284966056216949699382955996667487093821544331210360866357135093094596643176218454452087910421942692266596419254819149033307411770928779530577969195218740414781095865828076084113666631982372671269763780301714290166276603881109097475626929669677494076674787816555238050216394045465022611394061514539550480006542065538888286367933198159359106434189968908636520831976021163706436324344407072267376979285687420174538070990128175794614392246476941968269293001782365725241890604711739778091381717391018317309970056945065125297148541394224124341965563295737661418547060494030128696215718477628493391361964286068781482522206065307753871211010880258603825424286953430571975985920080372835455040485662871561073172121636372888049505902050469799101484114394198068759186122311234372086635077895891909643074417047467023842541032343429736277173012046321577892157499572311240554958682959630165825774205521806291271488574780563050693375455197436897844234582807069316163892555434140565134316245176982273649384918987790324958487106545911842243354023258675615445200991097431887201739516287842364555874629728668833715335239497044531195187155131502257973042746301610249176799061286193499684516699914053642548688417968946519189072697053409387349337143095905034593418860710764899536035548271622966744947913515788383069886158647443857570821511360876876491578414799768963324471468247908075018419685472726473511565258177801742622491664201774942697607407593986125283826915600899851593463751583213817618191370475727183469737260762425436793933517426782877895861223967566151422166746143924410652951809614057275169784396739017232532426121860377577106999193846099461275672629598208028239533335291620187561541363477490363998430514734400754013472133489970013285650010298791250493733841862181848860191180208447732016313623938936945053395139024255086561976979766373823638551078796673980597666215607162937254055732222491258089561279485132737422964113351359407644784417703645932573108255395079659212082378084231743788237955012163364711831284551851695590014430088481764002450755936687619254272232320022279464977636309446874317770872011068675451211157966318385364777193953618739067883616464191790501816390293312012583140861932104215047066629021201735911127537078785683445460780865359781445364452923289826814092538406862590958262790695296916181153839280598334705774215106945050555603654608178665319021715431688148623095024981632546737492750686468089591082367523116077254414050071230550788752063981608169586804929184374149477965025051939811204134763170217913437965258339471084472809023716251967405450328628096496699960708014067522564527458097856964054065683356604288923945622421046444202767520148062556240584698454977373347361369535369339898834543202737483511584232365266372726266531479742012635984612349733579442581756977241759112668553911055304471091015102245704579160277920589918011742988450837046085877837728841915304149354158778456351055139220880296353860858795523848351485463605430038045834488982718056714394039235041544104192385382165514117333859905536147396036242703336269544656229035785588222614248874841216159054643321144505042039613754689716193425631203928121094481040211030374037179572584695254558790005232668575542793372197574544776291567535201571838240117561140760138801532701806820831500944932148938301773873565740121117520945750882950369835402416749491717483661889035018770122716688079719078476389802870894285955972045972730560660947128559264873277886289257425431444211139738067045885031975528664205548432260166764487787239217847393467803821617276056991842728680026728222385203820619715000878892684706936758063226300920927918196766589157173417149131344337146835485692539070706930276820536430100662835934107712941623887640850938113826239120444527927681898101112516151273317761453132443273386757392619042949186620086313661249198661786090920794793536812268178136216035228397998443255571580396139742366317218073600177425686299193342173994714274201943613453672126365756327777397414097342821236072549373170002975374220732058885031178505528915454196361897675380419461243035502931760969826556718964080684134549615822706674455241961929534180074676059636273827134346402112349709624509336730463018980193547729681254189972048542550589945617697914525432656731988967071754533434188633819502812628345621094539160925318469662025989643772428544557080948024238726901288740596952872867889212106717047813182799189485176217747549245158488977097936765388053937073790550568379062830580488701628107475431260187572721861653736578515050306437314588867042318197948565597451184744543247701730434200971737067631018352324418453093212586202288589344699232298599830380930150109045724849070021034282377502623749211817744749864494621693855320243527311907084645019378774216453037961071902566099928896249006529317437737985614709600244357109151016799680261843906040497108335647236226465749261867928668694450173917773240396672584350431876804317195431670438696343589766549980919473542887678423871768524434725883369549328160660858832296960451907063215023392597372812400677768494917419060211170452614871670439032795892115234371754134311554677847356760503952329764196463921607532230481978321207638484876958613156114404536858532582161976759066707367712697663831249338223132022750752933990403720685608931135532827032542784356334896690925400784608972351786512291882095847037597304759049900122222531215110882734310534424538981156277080081454987931583259047172911631949284674488548863769608899983099119599037003019508470451371892715985808721122272039277416717098589089152466694017045908779490550478504942603215931641430690647706787371654977692756021300585277855785942560229426248370329066071540256504549601227377311438137211439301776636981738681735540481837787855648338423482667333301586254952626771536974352088528698533120394961336944571090844833686110351869195809469560567962442273308607628309245313479387551778000191875607721282741872527814817926223913687735109598762453857561384695955948681832600967463149370969675169237312794700559863912908166604727770940430607504005518324104688575861027217068#6903411946"""
l=list(s)

print(l[-1])

out = []
i=0

if len(l)==1:
    out.append((1,l[0]))


while i < len(l)-1:
    count=1
    j=i
    while l[j]==l[j+1]:
        count+=1
        
        j+=1
        if j==len(l)-1:
            break
    
    out.append((count,l[i]))
    #print(out)
    i=j
    i+=1

if l[-1]!=l[-2]:
    out.append((1,l[-1]))

print(out)
