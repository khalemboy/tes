    marshaled_data = zlib.decompress(compressed_data)
    original_code = marshal.loads(marshaled_data)
    return original_code
AsepYusup = '654A7A7466657432323069533575355036536D793063634E7373773771527339476F3873533762616B75793235484C5057426F735343544A4E454541786B5553726549352B777837646E2F50492B772B307A7A422F746E2F4778475A414147516C4651753162566856306C415A6D526B5A6D526B5A4552385366722F2F556674762F365850374D7A4E2F4C376E50576D624D385867372F7A71572F32585975766E3754594C744D2F39567A62596A36334C6E58325A335A793848377639667272467074584458334F486170386666545876512F7236323965596558465462503371666C73707A3342716A6366546F394F5836322F2B4A4375366C445669365033304F6844706D6144616A3663767671772F6934316975755243446C3139664C67634F2F4438666E3665756850752B734D2F6F694A352F6F6863344D4B444C624367696B386641356370384A434D5945437977793566504C356C3467485955444E427234375962376F6A327165365841375A764D4F583349456664634A584A76484A507679645A3366394C6B586C67376F6C38414F332F42707A7A56393638674A75653948586C686D5A7343344847637934495235354E75323645482F667041772F784B3549552F4944454D5747305A4A64774F395849505A685878534775673331724471657478686F7A4430676D3639666D33574A72792B32647265324E7263326D77335773334738354466684C7648522F7348703263485431714E672F66763337364833302F61652F447A6C726F7142614666347558795443386E76664962455A626B36342B63342B396C617574393277774364697A3633416B3454456B4F332B4944484A636A634651427477646C5676316E64756F3671656C6863633053506B6674424E3079363148412F627274446F576A35366967746B4A5053434B66694136616C716974587137414539624B4A386D6C6E47577A37334E51345A66434C2B55722B426947487542383474485061576E343832476A39726C4262544B325642324E4C693059584F477542324B3570773137717466317079795A31325077534C2B54444A597A54615A4A3038374E5547334C55726E6D2B63494A515A457548486237726A5837645075364E58754B543566734262656A435A767769624446574442624B73427A4E6759544D57596C704F7878577942786D55564F4749325247497469576943642F696D31524759556A6D41393537304C7834757739336E667A3258664A3259516A55306E316A72575A536B324E38374E4462424262694342613535656244465176594447345642303576717151626F6B537A4D587A43725A304E6A652B53414C454D6D524534546D3044636E624D2B78324B485A357A3358486450414C7877554A4E41326D7668655930313249707A684D414C475861706F4E52713152714D526B37556B57537450317336537453565A4F302F57795A4A31346B356652445A494C794862694D6B5534544852765558444563694437617A764379396B782B62455A46306B6164593230717A5071635537376B2F4136447373336653632B7A33546A326879716C467173654250662B533641562B3638476D315530752F4C366B7A4B7934584E75617A717A6470456566766A575A3244654550624B5437724F54544A575953746F35706D354D49666F68784E41454432544F6449667A4B485076772F704A66566241573941642B4B59574870366B6B62384C2F45316F72654C42635A36695832544D365A5775427A626C586175453762574A6C6C314A6A4235377032626279733230747A5062586E6D3772456166627A6B2B332F5A7562627673527039764A5437667A6D3573754B6E4D504C6370506E2B317862726265623236797359333736584D397A3833562F62586E696C596266736C5978706D615033614B334135344E326555626536553844517473332F613365696D334F4630473249476F6346412B424E4A50666450346D4B6B716144484144464A36493435656E3736782B6E5278747558483737432F3633547336506779446D646E445A3272766E68596650376A3663762B626C39307673347576377738712F42763332776E5063747A7A452F2F4E766B624C6F4E79336B7935626258744134613475392F412F6C586D4F6537567451336841564764627664324E4A54506C4577396F66515A527743315A49487837314F54576C6B2B674C496B427049706B6B353741386E4C702B34546A69617533576A4B4B6D5A637450502B48735A686243464D77624B4F50617144586C59306D4A744D4432763176656E5867676E714250556841736C6F67377971752F31513345466F33314F597475396E66336C4863307A504C4C7742525952666D6D316751754B485A6149714A4A496F6F49534C35647247415A6D563437312F6443433465436F506D6C32347639726C352B3050766E4F466A78326D34334C5443742B34363171425655514441544C576F556D534B6C43527159536769345054527559494B3961344E6D67564670567934344F31776449744363422F7457656C4E425A5530334C4658776862764B52324A657A44464165784D42364D6E6E797231716D7A75485831786E6D754F7734504267646373714F6E554E387445787A494B6A79384B47454A5258734C3974777773666A757876694F4A5930764C48494136614F7138516D55783249774952717045496444544B56734765702F702B6164316F6A6B453356483744624A4961626F61375677707377363566686E7A7643695A505737452F53723850486552434A5A6378304C4A4D466B57574F594E39627068314243477843774C44537743356149507744446967637871594E2F66647432474247714172455631356147437961324649794B77696D346D6C5639477539776832776E484379372B70524F4B687551367839375175496A7766364C57365532654C6B462F694278422F454431646843543969315A74365157312F784D6647506F51576767636C3349775633413856624A65502B54444B4F2F423931383849353176573879657470584375514F72576E3161756F5270746B694F522B52416D752B4C7034467A4636376E41465A51584A75575A45506D4A594342734B63676C55324969594F642B6C465557584548594633646F6741384C424B624E7971704E3576676965376E3653457A5065693669556C6C567236734554327A6A5A534A4F357541774C6165796279424E64774C6E31545438576F6B54524B6F4A764566435771665555532F6F78426D6A46787A4F5654474962446A64505252724C3541307356474A43654E335754737778397950717737785A54314A357358467444727236322F48466262765659424B6F473175564F44762B7671314F51366A7442484434784C4858634F3372363744532F7065494D7A365838327836574D6170347A6D6255446D4457787639636D6B2B755266325A50583353636E3353646E57704A77326E3937656E6A307172752B74723647436A4547683062354343596F784E6F61574556472F67706F48517073794F6B454D4D7356474271724E6F6C6F4C565A69566E70615A75635242632F6F4737457244713653474A7542674432426247613347744F2B617A5A6D34436477427A7945433141475A4A48796A4A706C484D362F5150676669763645687950586B714E377951646D5A496576515857344835544F7078356F4E5579546B6D4C7747386343756F766C6C485A34357761685467503065526A35734D50776555306655546E544A37574253697541336B3330697177464651793545316242415269474936546236585136635733412B39582B7142715A56633832517A77306B454C6263797A66465A6132514561317231783361484D49756D485275666273616C64727470746168576C5549714A4A75757A554459303939674B316B3470626E55577531596E626733324A7A4A3833633757657A7763676E6D72667456322F4776524866454B457468694F777067576331785663776A7A784B6F543936757762624F2B55577577307246776F70746E544D32494E527650324A7379322F4D386D332F6B7654636972472B307432727454565A36382F7238354C674354736959733165385033624C616F70316D45717467582F5A435132556E5A6B444F4E74567937796B5131677748415934582B444B6D476979366A6656362B76724B737133436A7554444479336E7656486D4C384E647A2B6348344B5A56327A4D50746F355A5042642F627534305055465A6936684D4862746C713832436D334151354262414363473067666D6846645638775769435177446966717548797A57576C77714670393434545375707558672F7571683148302B7247636E5577576661686A422B6D417259565750586C614539657A4C62714F324134646439634D5A50572F444D7A317336646834426A2B6B705879347875654F525A695943517054785A5878585A75616D44656F4B4C754E5A645357522F4E71316259326C6C56664358364E787131364C5379316C626158386E6E3037624B36682F7A5775594E79315135663165532B6E6266514C764B4750746979716F447A71782F3576426F66574E68713665422B375832374D4B443535734F597554344B4A33596C73342B78354F6C4E766E52694B3230574535684E33627753412F56347A587465584F6F3577777273616158736151614247447263716F4B6E4D384A444352612B31315A6259635836334C584A3732675162336748686A6945302F647561674A4F37745373724B477733483430776356634B646C7674515233486144767A4B6E7467767346326B626E6439705761495A686D71446D58615931744F796F6F41726E74364C4B78504C6D596A6C30676A5762697A576A414370384F5055686D75695053726F324D73474E4E674B497432434A74613557716E3333764B7A7072494B484F3432325842763634486D426935446A426F5A6F52662F392F684272587231392B334C5A344B36795934434362756E43656C7257483943705965414D7447557A452F6D7059596C476E42383249634F7770733579377633415831597836426C574741797A48643971737578576F347A45584B6750474D4A6E3836734C657071625356774B70766668724F7A41797247686B727335334B48485A6D692B386B3176394C646A62465668776C70515A4E32386769306A4C44705864616E56756C4A64576149326134704556796F6B5834457A4674776B42534F3079773951324658545756506E70645A4F57494A3259734842332F63506A6F3850547339546E562F6C4F674E743834526A774E70544E33663041705449645068352B2B7647734C767052423776645A73332F6138376E314E7A45526E2B66714B6A616736726D594E69366C4C2F31427743502F734F4A306B5953362B356F6371566575593766586C2B39757249456145776256785672584C7836654B796B6C6658326572784B48334D3856576C752F664E427451774A2B626A4D374154467A434B35634F34532B69305044396C315A43796831494C2F63675A61356E7963446E6A3843374774495655704865796433514B6534544A4864517A4859636E6D48775377576D61786E446E4A7664707075327453384D77575062502F4A3371384165307173504442667766467A4C6A422F614465714D365362414F4C33583241344F4A5151484430763847722F4F3343315A485971437334784D7767623955583549763671324F62432B67426678673657733536686F5252614176706978394F5368377279686463334542417A587130414F6A78782F775A30582B6F674C7153645A68372B6B4F76776576442F4D736A566F544A416A424E636B5944765A6F4C7546356D6B6A76323447756B69774F2B4345557134495051476B4F384D417875305A4273557853795A55714A3473455061797A55714E5A727246655A49624D4845634F6939313672476C427A5A356C73554E6651496A4E336F62754241786F67465674714E726E593759486266433941652B494A67427A47766A61576E2F6B696A366D6643563472464649723942696C374A4A6F4A356C4757677257754777542B69744D6B53494C78554D51616C72476E576357314246695543477474737A6251622B6E73456E707241526B41684E2B475678323578574746367775485A394B3167326335436A563856574E654847633859794B764C734B4A6C747331476267474D633868705759576B4835347776624749366B576E503535344D4A54563939702F2F362F2F38352F2F38373642377A58717233713533797177556A4957336D783542475757434D425349415563626A33775A6E3365715572484231577532326E4D4F716744356B44794952316953665051356E784D7A596A304F683641704E5143424E57594A71524D6C53337036624B4F4D454438793373415A6B6D677A484C553078794161343330516D573253744B59546D6E3653534A737A336D774151536A477963413347334D5631556C394D58636B356E6B6A6D6F334D462B33312B32376B68485133794A57364C5A5864383133596A55464A5047316D3151464A30696D69326B6179515941654268516F58554E4E69376E4952425945566A363432446C2B647953334A4D4871424E63377954376F736C76466531612F4A65597A466B546774574E5632725463766833503075594364697645566C5A4D68446361627A48666C795743384C452F6A6D6D6D334C6264363876626653394C64417042567A664F725158334A4E586B7070564452714E4459366235726656674B636278546F306C75755230574D2F597655504D2F3750336B6E77395561537A6C554B6F58383670446C634A495532306A304C77584F682B6D5353416376323147634347745551674A68376F4C6F5330683044472F5868593069444C4D7A437264313035322B7A39756D36735670534A52717853706B684C696236427535654744382B6B397A6576782B746B3441505A4E752B486D5170704141315444694B6C722F6B573259484145574561466F664A566469386F41644B4F7359747679734C6878784F43575350586932654B69566C70464E47625A63734E47375762474554584174694568732F785447554E4161614F674F6669436668377A6D757253566357797535456A383030697635745A66776139387A796D5A4447766F374239705A7772696A702F6534786D3531707250764E6A646D476D306E75673238754B456144546A746D3350546C543034704B57674D72706A6C63724D7163753743766E52736D72395474686942476F73755958434D73654D304A344B7568504459655467716D654F763571324F4967374635417177364674324F5A492B41734B31424E2B4F4C4C4D365A773250732B414E48556F53393164314C744565784831674361456435513059526C484C326D6F412B45486F53453948344A4761764D535977416A747158797770624E6B69554661617159514C756463356D783234523270733044777A6C4668535545437A4E4A424A444D42433855344A346E774B6947763344706D6A7662634553304775426E41413164523168435647484E466832396450417531726132792F4D426F67732F30472B427474746F576250714C5846567A7A694B6D54343347396D746C4177577A554F387148506245642F68684F50537338465A424133564B2F4B632F6D7769516F39645A32396A7042476B7632766C564E4E753342546D59744C74595455763652475750756B4466744E7A623271755077525365504863494A51705A337A44556175335068776B34556A55684B4E66306A5A5247677853774D4850617263775050684A7763316365504B306273496D724F435052726B382B3564624F5A715A5070636E63567450795176642F707A514B704B4B5A4B63365832726352784A326775726232667931466E6B6F74644B743369634D47597A55514365477537663061366250354149486E7576514255336174336A725A4A414141686E586C61366334467677504D756F776C536E752B7233334F4F4B326173624A7372324A365759516F6B436D6A3261504E425A42524A386F646C6D326D494657513162424B45556872776A6B785343586678304766735453616C304A494B6F39786D4F4D54564E71766A5575435147757172445345476130375578445367547553665A4E306B7336655441435A354D676C754D6F4B6939444A7665344B4D306D4262344A684F3832557A4A304667584B4F4B62762B6F6E754E5930783745623441577475646F636D73417972545A4C5470686B7639326C4D314C417959496E3635336D56484E34574A2F556E324F696431645965726D476D665355743548454A4B6E77582B5763684C5637563949704D665A696B6A42424B74726A744C505475376F6D462B5A5474396D2B4A494F46713369724F2F786177524673336D31384669664467306F6A4C6B7936773330434F7A3857415271424F32526757686136315456512F356F33386E543670497935437A38717A4D54543051416E55666967464D4575336A6F6F7A7855326E687A3038456D6E74634A5677776639637537513466354D354B412F593372744D3369577055397764747A4D646D2B6E4D7732764B37476243707469524541446B36336F6C70686869583649313670687A4F4336584A6276737A4D2F586C38794D746362594239544573384A484F5839714F4A4F704B336D76447533615173436E465875575246706C6D41497049534A5559414375524D53363643544D566C704978356749644C714C74656A684B32794232586545557157672B3448727432394C476E624C77485644346A4437556B63546A3848726B39614454516F3958614437522B653868436370484739325771426B3868656D763631634F7277334B343159714233583448663577522B5A37427646474B4B7A4A466851514B5458347542534144664E552B434F5441306246617A6F6F6B586C47343157477A704B736C72444671584E5273564D4F4533433656305043326354316E6C515230522B506B7169506471616565547A717172647033455730653156627457445776706B5258766D747A4238306D656D37526A56317868556733784131444C542F566B62622F685646392F6A495639324C72657461797A653732464236364763687671453569754F65544263762F687037674A3150594C336B706A45482F6A423359634F4567496B634774586336374246447A47334D476B71677363517665307A54546F56664B4D55677258693663587A416F7154574D4C586657435668364334544E46544B5668716A6C726A377072336949643779557037423270524C5147522F6834754B543970483358746A754F46415A6175454D6A314C77786C57714E49317878454F6642355A70537568467657624548343942726B43767562316C3874376D7A6B374C326D7074574B31425938443539766232526E396E6537445A327879304E6874624F34334770746E59624F7930647A59366738334E31726256334E6E614D6E644D50656D61507036335642707A4844732F3349634A6B6536487A5276313354483542624662674A375354666D70747173397863647057586B483542776B5333715067364469636763435A32542B3533636658786F7633722F39654862777674766F33733767507A322B4E45353371464F756D637233784448336E42325A634C774341634B666C32594339375534714C64344F7345716A384746706E4558634A345055385767346862594D674875634B6F30674C33774F524C476D4B4F686930776E5665654151687170355039794F303762777853674A326D50504F4E31703665597A596568506952526C2B615A766A6B4A744B3532653647423651596C4E47545268646146496E3446517A53553554654542615558326C5A6A4D4E6A614757785565383157723972682F5547317432333171747873574273626D38306450754158734573306B4959686E49464C725734764C693630655159423337704F5A4E73566645717943646E69415477734B6362725657592F704C786D747362306A64575636526F446A3431737451694D434B7A77304967634F4571345A6653394C4D473833416A366D4A5131726B78666D506C75674139516D46486F47756F364C726549596F414C74494C45374E6B3852785458344C72546D5A4C744A6C6258624B6B6C4C45776C475842675A53756B4B75636D424954394B416A64695A4771546F31676F533570796833366D416449493962394264622B34734C4670515A6539524B326E567674486B6E446B422F5A7A4D324C58346B2B5277334D796E72594D593076334668525054416E77703675716756744D4C67746871496E6242464F5163314E4F4A727A4852684946714C366B3756656E4E4143333841633848447159486F4A346539566C62485A7A645A507A5035494F49754439587758723549623373674E33547571376D356F524236612F41556938777173516E364A796461352B456B6F4F524844636550645A586A636E397844666B39316B4A504C79493173793042517A77416E30516843377045365A4D6E77576A796F754F5267674F476E7059466475306F394A34454972507859637258454A316D596E4E4841433532576F5537454F5A55306243756E734543664A593272796534424A393830426867503574646C4E6431396E4A6579757A61445A47527143787177394D4A4F7A4D39384D6F46726341664C637A7A346A5343427835356262683168523442364459336C35696D594F76306C6B6C4F2B494D512F734C49472B507778383178726C4B794B364A64784752736350313679554A6F584178513572704D334D6648796D5664386856456275623734436C336A4C4C686C4C4C6478594D564D77752B5737594963683252766976374347534C496451437A4A476B585435414A6665594D5859366C4E736C77427A464A58774A324F59754B7157324A6E453136776F6D504754424963446F4F7856562B364465705A516B5770727A4B4150654D5651594E6447536C55562F5A4B4C3346304335484876673075574F6B6839706E523379703953554E5169556B2B774973387276645249484B3362507348414C65614D4A77476158456C6E5243586B7377346D416B6B452F2B5546576D5A2B6E5267593442444147733679437A2B7A494C6A7A76585665593339434E56506E52634831792B434A61566F4F39384F316D6637463736566F364830426A34555276692B794271637743427464794851613542454130686A4D61357233494435785172484D4955692B57756F6372476B6F48455A56376C6F63574A4E7A6B37564B57375773376E4D5044742B7855416B7A3934706B7A5363736A70494B72667451424755626863576E6B3743344C47677866387766354972764343626977304755526676303776627049366C716C356668674C58696759594D64615A6D6746576A7A586D454C50772F7A4B3030354B6872586F65312B507A44424141304E5A4542765533734475624D45585669417A49484374525A527A5246526E71654272535963785562526759624A4454554B59484A48705361754B6731686D4A35624D47492B323565796746435476533237706778742F3450384C74672B4554483555667256674457515673497A7346454D773870344E4165636950533072386755484D4339727152334B55316A516E6234334433434D336E51657A2B546F6B76496C5578636F766D767777322F41356F6E4A346E49765445636D49334A6D47356E4C6A487250784E506476464B475348362B595347556F775939574A6F2B62686651733845676A756B57645555474A534E6B6E6D6D52705A4B526845334C5041447A4254734F526752544E6A4249795A75524F514636306F4A636D73435143635173587A4E454431664F5864347379697550444D37704C44646861384B5562637850632B6E6B41464E2F77542B65727876476F64686F4962353033424443336234534F72416B7965613343796F306E546B34524D6D686B584E514842364262747547424C647A67706745513953764B2B4669346A5333536B376F78563871707662546F674A4A2F596A39466F763342586D486D414C4B6A39534B304F6543545A4D503535524538434E624337734E6C7A3377684E48444D35665031547335654966306153746C5170653672585463444A4D734370303459726A3053415733627968676749485854787937656258796C32685842677439684B3635704131576A50445477754133524431624F5A6F70307777394B526B76633162514762484E7159483538714750377568392B70685762642B3945677570412B77786A67344D75753654337878307332314F677863336A4356794A51384B6C416458486D4D354F677557576D4F69644D6E7477764D5750474E517251554230734A6B6244462B6C3961537641677052574B59354262484A6376506F3666634D584B7779616E4261797467506641334A754179547359794C59785A774F6847596A695378672B4F7459586A5275576A4248354153323752542F687A66322F5065482F7779766834634C7A2F397554414F4E742F66334277696A57584D5839703436587A4A74317065635251762B544A4C42347A7157475230425A35724769773049304859726B322F596E6169666531514D456A4E474C303852572F766D50656245593552336C385A704F4F574A5334696D52595A4B4370306B4D55766C427165793533624A4B63424E4957306236586E61684C6F4F544651583054696F354F7A772F656E2B34644737444B49537A5131506A69326542362B575070356D766439755A575936765A336C6C4A48434E41635A36313164727162472F734E4C63616A635A47697A716552307A7834692F6D754A4B61612B4474442B67516B6777332B70767464712F5A723235316D7476567A6B357A554E31756D6C6131333971306D6F67706446706231493037474E6759667331505A575574453935674537695065524633776A317A6542637052697A716B3641713671417A49746C78554462456E41463441754151673576714C7965412F6159715648784E693652674535726659637334504837376B61615169506A6F395044396E6E482B2B75446B67496A6970645A6D754A446B59556F726C456C38553452434F6F4E74744B6535363242504E656F456F35536C5250483130706A4F68626B455045546E5848564152544A32774D614B6E5738614C737A49687A3275696D657A6D545A4C62714973755457562B37513951693132387455522B4A5751355171625836364B6B5270696962733744613852614431594262435A47426256723375496839587063356A31352B437943327358616D7455584C752B766C5A5063484C5577446753316C4B6A706E2F422F625272456D72374638506F6A6139326278664173566B4D674D2B2F63444D5036616E58436C75385A35475A6E76716B7A734A7478422B506774794C592B43505A546F536D354E734E4A756E54696C4C596E38793065313937417338354F4B68654D69635851474946494249415967556745674269425341694C536F42534253414349506F436B416B5149514B5143525046454269425341534A61714145514B514B51415241704135486343694568584F5A4F3754496473425637796548684A3632664453376167795561723059426D42563779532B496C69573343637761575A5949546B682F38794838736F2F77552B31767576435554756364706B33535041617667703159652F324D726A7750572F4A493454627941767878576B344670314364744370446D4877696B53556B732B5471566C4D414B3643624C735942754375696D6747344B36476168714942754375696D67473465516C4E414E775630553041336561494375696D676D79785641643055304530423352545154514864464E424E467270702F317A517A58617A74645065376A51617A56616A6747352B536568477055546C78356A417A446C676E565476326152704171696F426642474C676A4F6953593947426A75307373436B336C555445624B2F5664435A444A666466625958794732325773304E6E64322B724166656150614D626533713733575A71634B43727656477A5461375761374C6332504234476634334137316B67765068546C4F3336446E394C7075536C7062573574622B5033576D3975504F78377950424841513339776143685A7577754662685167517464464C68516751735675464342437857345549454C466268516751735675464342433657306F384346436C796F7749554B584B6A4168663578634B464B7576582B3239507A7666317A343933626F3150342B667274366345394E41636E653066485746336753342B484C33562B4E6E777054676F3347385658716632692B464A616E41723957534A6F56555071663548364F6A5571654A7171544C6C717952516F58696474766C4177464368694A7668577863743941686A6D4C43576B3742456B4F386D6634636D41706143526E517A34384641324D502B492F6F6A45314F596B4938793742476A4636474173507358303249675A7461706C674248354C2F62394F68686135743846656D774D62594E766D62334F594B5061354E73623155356E61377536592F5547566241383758616E595732332B7533664A2F7956616842762F356A32477743784A4D684C6D4B784378755A485A67474E58525451324555426A5258515741474E3559525851474D464E4C5977355149614B36437841686F726F4C454347697567735149614B36437841686F726F4C45434769756773517A4E7537327A7334397633372F457367497A657A7A4D624F4E6E77387A616D35306D2F764E447257617A774D782B53637773465144506F6248466E4773614A334F67564F466B2B517A6B484B78617A44356D6B62644D766D39696F68674A47727654515A6453755365726C76547A6F4A7A5748436C6367654D39364743615932634678505A6F4542736D794B7170364571426170373359784331627758555576332B46447A74323033544136334A6A7A4D574255425841485158767768416C787062584A3461576F486146616A6433645853452F3930755A43524B6A433741724D724D4C73437379737775774B7A57305651594859465A6C64676467566D6C2B684567646B566D4E302F4847616E677163437353735175774B782B7764463744595845534B6C45436F6648532F413264373342386B71474B414C4C77394F7A342F326A732F757759384B774F4D50416E6A41476B61664932474D4F636F6E4D70302F454F7842787A707547617841374E6B7945644D73414A48456A302B594649424937426238664942496A4B426646476849675959556145694268767868304A416B384333516B41494E4B64435141673070304A414344536E516B41494E79564156614569426868526F5349474746476A4941394351544D58714C503146675A73384A6D36792F5644634245684F7A6F79336838625A776676766A2F595043726A6B46344E4C51496D2F435348353569395A632F4366414A494A6D446B344D7254646E6D6D7A742B4D4B322F6371374243327A654E3938397141383633746A635A4F6C6264617257716E32654C5648584E7270396F303232322B73546E6F745473534E7147414950366577674C554B45434E69774C556B43355341576F556F4559426168536752674671354F787041576F556F4D5944614170516F774131436C416A543153414767576F6B61557151493043314368416A514C554B45434E41745434505941616A2F723162567674356B366E41583836786465332F64722F354E47336933505A6438456C535A5630535935414A6C506D332F306D6A38376C45656679723343624E37346A4D3562517749464753546D534F70376E30674265794838454B5A656A4E4262546B716C2F4857726C57554F37636C5A387039736A5933597930316454667449762F49386C31554A2B45384A4578594270635270787A4B63616952786B68424D6D5445384B467632476F35664133656367443950766A3071364267476A3169316457452F4C4D43427355464F4A67354A2B63614658644C3163727046684B54584C4353635A73395447344753584E716759686E444E31614847646B45786D72684F6B7462693859787732536E6D686A5833444B51747A55457934674E52523535543633354F6E683046442B445576704E54737748755552515365576B566934354F386C7A7A494159425A644C59726335303974336D786B79724D4F355975436375664A326172364854586774737A7230534843573170705467576E6F495A41464C4F6973394C544D73366A4A6464523377376A66496A3137484B715551434A6F4854554D374E53636D3832414C445350485A4B427645527644547861672B385A43384F4447374D7130515231516652593167594571304E796C446A372B356C2B747048314B4C7536574C70536159682B535761476376332F6C4246377271554672326F5576783832324E6D66724450794974327876662F2F746839507A3958563252696B46686E2B363746505074533351464F76796B45342B2B583439417257365847666E4D45507737435A656C765432326879483053784C433775444D376241396A59482B7339597169532B4E35426A645544727359495643535058344A30435A355932694A4762584A7358366F68663269614231624F4E514D676758566F4A464E665433575A38455353314A76666341306C55433355437A724D6B7055494B7776355A795164665A6E4956573431463755767058724E4765315365645542796938505456556F366E4D4B6D304C4D4874563652464F434C65694657347946594834555475774C487461324755372F426B7163332B644B4A2F657A4C62714F3255784554384A37723570555971456659536C3563366A6E44796E6631373468304F384D6741432B515731562B49784E787A363532653230693238714D7177724238544143586A684159565750586C61457058726D547658446D574C4E6E55786A416D65724B6D796D715A733356654379323141456C75646A635575392B6E7741305141567266427179456D7430776578705774645630304433712F325231575057415451702B3336315143366E39435962596A50777978705A474B46396F72795132782F424D3471313041415772506468425857714552456B33545A71527361652B79464432634D466263365770357064654C32594F3869372B664E68636F346771477539787A4C642B4741536C47526F775A54433067564C4C636659536930514441426655514342785A38434137624167466D47704167414474514263304471533351344347554757626B4458315132796F456B427843553135564B6245417152496961495672364E4149543979767772624E2B6B617477557248594E4A766E6A45314C645A7350474E76796D77503149312F354C303349717876744C647137553157657650362F4F5334776D77783575775637342F64736C71414F6769363173432F3749546B794D374D67656B4C31564B4E345572776130794B56612B465252363076724D74565771476535726972325476346132774F7A5471756356645965346D532B554F4A50586E63634A5133674E4A753935774E7052574D59787A742F53766A586F6A442F3151477447752F4A583478627679743352373062776D646950344A734D424F2F78524E71304B543944727835595A65314F466B4B474B436C794E6641685A3043356171703353737057536676416558785467483365486732734261377471652F6464502F6752572F7533734458427667633971796F7373686D746E633757566C497A364658746743714F77752F502F4F324A3647775932316458703936623435636E4C7A5A794F37695A37414B564C384357747A4F3968754931773751334A6E75494E54614965684D5236774C6D426D42505330674961796E4A7079706C566C6F754250424A646F4155663734764C432F48593851514E786B67707637435941694E3072456F466D6E6457343053455670584B39572B653134475855422F583971556C4C3876752F3573666E576C6173775A2B626F4767514B3059367152616C4F754958546B515565366169326C6D78374338646C4C72584C7836654B796B68724770332F584C702B5774646D64497A454D6130713757592F662B34476665596654416438375363466745715A5043734D774D2F547176426E6F74366E49614A617A736746665348486359796355416F624C57382F62326D6265324159715330465A46705671774E776A32706E6E6339524E35542B537A454D384E6A4C56715254457A785937797074487353685144496475364C36543935464B7162376E67636A654F425144384E394C355A38576667777856336435466C4679394E34495246492F4E415A52314E385168587951636651715A6B715A636F4749464F4B535275777347734D7973424D2B3655566D794643344D666E2F2F592F2F38622B58526A33702F6834593936536250447A7953626461456673736F5A543673444A45656A756D41476C7444572B314D4C796E436472786E6944436F48374B722F66362F656F745A6967706D4848633635493344622F57384F3272362F435376686349732F35585742732F4E44474C42746F39774E71532F73537150706C556E2F797258703756777074517132696D566D5A6D774B3539476342662B37567263474934394A685A7268386570676B2F3541543451313430503651583559654D4F4334634F583059517439324135374B494648652F437961544578663568677A752F77526776683042372B4A5548374A4A70717A5772714666672F422F37346E4E6675506C33723559362B58537459734F3978696A49434F576A455A776B4649466B742F43656432336350374472425A513751326D4D6E313958494E6231476753345233576842304447696E55774C45674667464D374467303775546D727A6E55674B756C4C7278703933454B7362786275314D6F67386C736D4C4B69416E7247374F34344E6C38776159554E6337786D6D7665792F6F7A3672597875534C4332723056466F4971533845534D6D304A5870494B65644D5A593554564B392F30526E38374267666D5334554A71357969546741704B6C76543438764F354C6F4C7178495830366353354C304E714E4132746A525A4E5A504D73413346712F714167714B53546A4B7666666147656755456234746554636D3142712B306A4D6D71784D74576E736D427551454A6974772B375435426752373077386A6E64666D52696270326C374157676E424741392B6C6E796C4A446E723564646177434E316D5847644E4C54534D4D4C2F4B4B6942343041706B506E6B6D42553058307A3142643350775970774E6530384465623848307A413967636A446435546745314A67615178387752334C6E744C46424B5258323267666E4E705150622B54636A726A34556B6B3777596C6E4F694B537739454145302F4236355473364B4A463552754E637156592F42696868426B39434A79736F566C584C5641464F6B2B30445469666A735751666939344E66765852655246676A584B6E32737238567148537243476C36387146774A4D33577673644C6361753173626E56614F7874624F35334B356B367A302B6C556D6A754E78736247526D74726332657A73376C647159426E305463396D6B4258673563457534342F574B4E3163624777776850716C684232713356507759577061484D56313770496C7272666238425152793675383848666A38374F6A30356661646C3675514F672F767A6F354F44343650514136674E594C4C796A35377565676265565556346A6A6F6B49684C6F31796B37523077334336746F5566733471386F497874674537427645684F38657261686F497A5057546B616B4C42524F31586C53757454526F4C594A3373486D3037694664636346584F5569744B2F6B456E4944616378587366546839632F723234796C4B7A675846576C464845394736375971475956313870637833544E737776437644554832387768745834696A5968306A6E304262656762774354793369363252715A4C4E7972474C717335526866495353567550317645514A4C626450453252616137765A626F454B74427274526D4F377664585330715A474165422B4C69786373412B774E2B704433485A66374C7165437667532B30446D4B72595173545756526E3741596B5034446E564B543844447843644565773762795745444C653245762B442B79417A67384A3377696366396E756C48416B492F6943736B762F52704B4765562B43734C485045306657554F7A522F42624130646F42744D2B3745442B6F555942687865736F64763434396B32766F36794D516738324959424D735A43495935686F486F484436424E452F326A6B3778764D5858326F5137456277674750506E4A52387A58662F2F6E4947546B773D3D'
hasil = AsepGanteng(AsepYusup)

with open('sc2.py', 'w') as file:
    file.write(str(hasil)) 
