---
case_id: S10
role: student
version: original_pt
timestamp_style: none  # none | start | range
---

# Interview S10 Transcript (Portuguese original)

`Interviewer` = interviewer  
`Participant` = case participant

Portuguese source transcript. Working English copy: [[S10_transcript]].

**Interviewer:**

Boas, então começando aqui a entrevista, podias me explicar brevemente qual foi a tua relação com modelação software, isto é, onde aprendeste, onde usaste e em que contexto?

**Participant:**

Sim. Eu estudei no Técnico, informática, acabei o curso há coisa de um ano e meio portanto ainda me lembro mais ou menos bem. Tive modelação em algumas cadeiras, principalmente Análise e Modelação de Sistemas, mas também antes disso já tínhamos diagramas de classes e bases de dados. Depois no mestrado e na tese também voltei a usar alguns conceitos, embora já de forma menos rígida.

**Interviewer:**

Quando dizes menos rígida, queres dizer que já não usavas necessariamente a notação correta?

**Participant:**

Sim, basicamente. Na tese por exemplo fiz diagramas para explicar a arquitectura e algumas interacções, mas já não estava preocupado se tudo seguia UML a cem por cento. Era mais importante comunicar bem o sistema.

**Interviewer:**

Okay. E voltando à universidade, recordaste de algum momento concreto onde tiveste mesmo dificuldade, confusão ou frustração com modelação?

**Participant:**

Sim, lembro-me de uma situação no projecto de modelação. Não me lembro exactamente do domínio, acho que era qualquer coisa relacionada com reservas ou serviços, mas lembro-me do problema.

Tínhamos feito primeiro uma parte do processo em BPMN e depois tínhamos de representar o sistema com outros modelos. Eu fiquei bastante confuso com uma entidade externa, acho que era um serviço de pagamentos.

No BPMN tínhamos colocado aquilo como um participante externo, numa pool separada, e estava bastante claro. Depois quando passámos para UML eu não sabia exactamente como representar a mesma coisa.

**Interviewer:**

Mas a dificuldade era o que? Não sabias qual era o símbolo ou não sabias conceptualmente onde colocar aquela entidade?

**Participant:**

Mais a segunda.

Porque eu percebia perfeitamente o que o serviço fazia. O problema era perceber se aquilo devia ser um actor, uma classe, um componente externo, ou simplesmente não aparecer naquele diagrama.

E lembro-me de perder bastante tempo nisso porque tentava fazer uma tradução demasiado directa do BPMN.

**Interviewer:**

Do genero, tinhas uma coisa no BPMN e querias obrigatoriamente encontrar uma coisa equivalente no UML.

**Participant:**

Exactamente.

E não era assim que devia pensar.

**Interviewer:**

E como percebeste isso?

**Participant:**

Acho que foi numa prática. Perguntei ao professor depois da aula.

Eu não costumava perguntar muito durante a aula, principalmente se ainda houvesse muita gente na sala. Normalmente esperava um bocado pelo fim.

Ele basicamente explicou que os modelos estavam a responder a perguntas diferentes. No BPMN interessava mostrar que existia comunicação com um participante externo durante o processo. Num diagrama de classes isso podia nem sequer ser relevante.

Isso desbloqueou bastante a situação.

**Interviewer:**

E tiveste que refazer o modelo?

**Participant:**

Não completamente. Esse foi mais um ajuste local.

Tirámos algumas coisas que tínhamos tentado transportar directamente do BPMN para o diagrama de classes e reorganizámos duas ou três relações.

Mas não foi começar do zero.

**Interviewer:**

Lembraste de quanto tempo tinhas perdido mais ou menos antes de perguntar?

**Participant:**

Não sei ao certo. Umas duas horas talvez.

Não duas horas continuamente naquela seta, obviamente, mas estávamos a trabalhar no modelo e voltávamos constantemente àquela dúvida.

E também havia aquela coisa de cada pessoa do grupo ter uma opinião diferente.

**Interviewer:**

E isso para ti foi frustrante?

**Participant:**

Um bocado.

Porque não era uma dificuldade de não perceber o sistema. Nós sabíamos o que acontecia.

Era mais aquela sensação de "eu sei o que quero dizer mas não sei qual é a forma correcta de o dizer nesta linguagem".

**Interviewer:**

Okay isso é interessante. Portanto era quase uma dificuldade de tradução.

**Participant:**

Sim. Acho que é uma boa forma de descrever.

**Interviewer:**

E quando mudavam de uma familia de modelação para outra, por exemplo BPMN para UML ou UML para SysML, sentias muitas vezes isso?

**Participant:**

Sim, mas depois habituas-te.

Inicialmente eu tratava os modelos quase como se fossem versões diferentes da mesma coisa.

Depois percebi que não.

Alguma informação transportava-se, outra não.

**Interviewer:**

Consegues dar-me um exemplo em concreto do que transportava e do que praticamente tinha de começar do zero?

**Participant:**

Nesse exemplo das reservas, o que transportou bastante bem foram os conceitos principais.

Já sabíamos que existia um cliente, uma reserva, um pagamento, talvez um funcionário, e determinadas operações importantes.

Portanto os nomes das coisas e algumas responsabilidades do sistema já estavam identificados.

Também os requisitos ajudavam bastante porque eram mais ou menos independentes do modelo.

**Interviewer:**

E o que não transportava?

**Participant:**

A estrutura.

No BPMN tínhamos a sequência do processo. Primeiro acontece isto, depois isto, há uma decisão, depois existe uma mensagem para outro participante.

Isso não te diz automaticamente como criar as classes.

Um gateway não vira uma classe.

Uma lane não vira necessariamente um objecto.

Uma task também não corresponde automaticamente a um método.

Acho que foi exactamente aí onde tivemos confusão.

**Interviewer:**

Portanto chegaram a tentar fazer esse mapping quase um para um?

**Participant:**

Sim, inicialmente.

E ficava um modelo bastante mau.

Tínhamos classes que na verdade eram acções só porque apareciam como tarefas no processo.

Depois tivemos que olhar outra vez para a descrição do sistema e pensar mais em entidades, responsabilidades e relações.

**Interviewer:**

Ou seja nesse caso alguma coisa teve que recomeçar.

**Participant:**

Sim.

Não o trabalho todo porque o conhecimento do domínio já estava lá.

Mas o raciocínio tinha de reiniciar.

Não podíamos simplesmente converter o diagrama anterior.

**Interviewer:**

E ensinaram algum tipo de rastreabilidade? Do genero este requisito está relacionado com este use case, este elemento BPMN está relacionado com esta parte do UML.

**Participant:**

Sim, lembro-me de falarem de rastreabilidade.

Especialmente requisitos para elementos do sistema.

Acho que na ferramenta também dava para criar relações entre requisitos e outros elementos.

Mas sendo sincero não me lembro de fazermos uma rastreabilidade muito rigorosa entre todos os modelos.

**Interviewer:**

E nas práticas, como funcionavam normalmente os exercícios?

**Participant:**

Normalmente o professor explicava a matéria e depois havia um exercício com uma descrição pequena de um sistema.

Nós tentávamos resolver no papel ou no computador, dependendo da aula.

Depois alguém apresentava a solução.

**Interviewer:**

Iam ao quadro?

**Participant:**

Sim.

**Interviewer:**

E tu ias?

**Participant:**

Se me chamassem.

Voluntariamente acho que fui uma ou duas vezes no máximo.

**Interviewer:**

Porquê?

**Participant:**

Não gosto muito de falar para uma turma.

Não era propriamente medo de estar errado, era mais não gostar daquela situação de ter vinte ou trinta pessoas a olhar enquanto estou ainda a tentar pensar.

**Interviewer:**

Portanto se tivesses uma solução pronta e soubesses que provavelmente estava correta mesmo assim não te voluntariavas.

**Participant:**

Provavelmente não.

**Interviewer:**

Interessante. E quando o professor dizia "alguém quer vir resolver?" o que fazias?

**Participant:**

Ficava calado.

**Interviewer:**

E tentavas resolver ou esperavas pela solução?

**Participant:**

Não, normalmente resolvia.

Eu fazia o exercício no caderno e depois comparava com o que aparecia no quadro.

**Interviewer:**

E se tivesses uma solução diferente?

**Participant:**

Tentava perceber se a minha estava errada.

Se fosse uma diferença pequena não dizia nada.

Se fosse alguma coisa que eu não percebesse mesmo, provavelmente perguntava ao professor no final.

**Interviewer:**

Nunca interrompias do tipo "professor, eu fiz isto de outra forma"?

**Participant:**

Muito raramente.

Talvez se já alguém estivesse a discutir o mesmo assunto.

Aí era mais fácil entrar na conversa.

Começar a discussão eu próprio, não.

**Interviewer:**

Isso alguma vez prejudicou a aprendizagem? Tipo tinhas uma dúvida mas como não querias perguntar acabavas sem a resolver.

**Participant:**

Sim.

Principalmente dúvidas pequenas.

Porque se fosse uma coisa que me impedisse mesmo de continuar eu perguntava.

Mas se fosse qualquer coisa do género "esta seta devia ser assim ou assado", às vezes simplesmente esperava pela correção, perguntava a um colega, ou mais tarde acabava por pesquisar.

**Interviewer:**

E partilhar uma solução tua com a turma era desconfortável?

**Participant:**

Sim, um pouco.

Partilhar com duas pessoas do meu grupo não.

Mostrar ao professor também não era terrível se fosse individualmente.

Agora meter no projector ou ir ao quadro com uma solução que ainda não sabia se estava certa, isso não gostava.

**Interviewer:**

E quando eras escolhido ao acaso?

**Participant:**

Ia.

Não era nenhum drama.

Mas provavelmente falava menos do que outros alunos. Fazia o desenho e respondia ao que o professor perguntasse.

Não estava ali a tentar explicar para a turma toda.

**Interviewer:**

O professor ajudava enquanto estavas no quadro ou deixava chegar ao fim?

**Participant:**

Acho que dependia.

Normalmente deixava avançar um bocado.

Se estivesse completamente bloqueado fazia uma pergunta para orientar.

Não me lembro de ninguém ser humilhado ou coisa parecida.

Isso ajudava.

**Interviewer:**

E em relação ao feedback, sentias que era útil ou muitas vezes era demasiado tarde?

**Participant:**

No projecto foi útil.

Nas práticas era imediato portanto era fácil corrigir.

No projecto já dependia do momento.

**Interviewer:**

Como assim?

**Participant:**

Tínhamos entregas e depois havia feedback.

Lembro-me de numa delas o professor ter apontado que estávamos a misturar duas perspectivas no mesmo modelo.

Acho que era BPMN.

Tínhamos representado uma parte do sistema interno quase como se fosse um participante independente quando na realidade fazia mais sentido estar dentro da organização.

**Interviewer:**

Pool e lane?

**Participant:**

Sim, exactamente.

Acho que tínhamos uma pool a mais.

E depois algumas mensagens estavam modeladas como message flows quando deviam ser sequence flows porque estavam dentro do mesmo participante.

**Interviewer:**

E depois desse feedback o que aconteceu ao modelo?

**Participant:**

Esse tivemos de alterar bastante mas não abandonar.

Foi uma reestruturação local grande.

Mudámos pools e lanes e obviamente quando mudas isso tens de mexer em várias setas e eventos.

Mas o processo de negócio em si continuou quase igual.

**Interviewer:**

Portanto se tivesses que classificar: small fix, local rewrite ou abandonar completamente?

**Participant:**

Local rewrite.

**Interviewer:**

E tiveram tempo para aplicar esse feedback?

**Participant:**

Sim.

Acho que ainda faltava bastante tempo para a segunda entrega.

**Interviewer:**

E utilizaste esse feedback só para corrigir aquele modelo ou mudou a forma como fazias os modelos seguintes?

**Participant:**

Mudou um bocado.

Depois disso comecei a verificar melhor a fronteira do sistema antes de começar.

Tipo, quem é realmente externo, quem pertence à organização, o que é o sistema que estou a representar.

Porque aquele erro tinha vindo de começarmos logo a desenhar sem definir isso muito bem.

**Interviewer:**

Portanto criou uma espécie de nova self-check.

**Participant:**

Sim.

Nada muito formal.

Mas antes de começar outro BPMN eu fazia mentalmente essas perguntas.

**Interviewer:**

E feedback de notação, tipo uma seta errada, também resultava em alterações posteriores?

**Participant:**

Sim, mas isso era mais mecânico.

Se me corrigissem duas vezes a mesma coisa eventualmente decorava.

A parte que ficava mesmo era o feedback conceptual.

**Interviewer:**

Agora AI. Chegaste a usar AI para essas cadeiras ou para tarefas de modelação na universidade?

**Participant:**

Sim.

**Interviewer:**

E como usavas?

**Participant:**

Principalmente para confirmar coisas.

Por exemplo fazia um modelo, tirava screenshot e perguntava se via algum problema óbvio.

Ou perguntava se uma relação estava correctamente representada.

**Interviewer:**

Mandavas mesmo screenshots do modelo?

**Participant:**

Sim.

Screenshot e normalmente também uma descrição curta do sistema.

Porque se mandares só o diagrama sem contexto ele pode interpretar coisas mal.

**Interviewer:**

Consegues dar um exemplo de uma pergunta que fazias?

**Participant:**

Algo tipo:

"Este serviço de X é externo ou interno ao sistema? Faz sentido estar representado como actor neste use case diagram?"

Coisas assim.

**Interviewer:**

Portanto dúvidas pequenas.

**Participant:**

Sim.

Nunca pedi "faz-me o modelo deste sistema inteiro".

Até porque não confiava assim tanto nisso.

Se pedires um modelo inteiro ele consegue gerar qualquer coisa que parece bastante convincente, mas depois tens de verificar tudo na mesma.

E numa cadeira de modelação isso também derrotava um bocado o propósito.

**Interviewer:**

E para além da notação usavas para conceitos?

**Participant:**

Sim.

Às vezes esquecia-me da diferença entre aggregation e composition ou entre certos tipos de mensagem num sequence diagram.

Em vez de andar à procura no meio dos slides perguntava directamente.

**Interviewer:**

E também usavas AI para perceber próximos passos?

**Participant:**

Sim.

Por exemplo tinha um conjunto de requisitos e um diagrama e perguntava qualquer coisa como:

"Qual seria normalmente o próximo modelo útil para validar estas interacções?"

E ele podia sugerir um sequence diagram para dois ou três use cases principais.

Não era ele a fazê-lo.

Era mais para organizar o processo.

**Interviewer:**

Portanto AI funcionava quase como um colega onde ias validar uma dúvida.

**Participant:**

Sim.

Mais ou menos.

Mas um colega que tens de desconfiar.

**Interviewer:**

E usavas para cross-notation translation? Do tipo aqui tens BPMN, agora transforma isto em UML.

**Participant:**

Não para transformar directamente.

Mas sim para perguntar o que devia transportar.

Por exemplo:

"Tenho este BPMN e agora preciso de fazer um sequence diagram. Que informação deste modelo é relevante?"

Ou "quais destas tasks representam interacções que vale a pena detalhar?"

**Interviewer:**

E isso ajudava?

**Participant:**

Sim.

**Interviewer:**

Voltando um bocado ao projecto da faculdade, como era trabalhar em grupo para ti sendo que dizes que és mais reservado?

**Participant:**

Em grupo pequeno não tenho problema.

É completamente diferente.

Com dois colegas consigo discutir normalmente.

O problema é mais apresentar para muita gente.

**Interviewer:**

E como dividiam as famílias de modelação?

**Participant:**

Inicialmente tentámos dividir.

Uma pessoa fazia BPMN, outra requisitos, outra UML.

Mas percebemos que não funcionava muito bem.

**Interviewer:**

Porquê?

**Participant:**

Porque os modelos começavam a divergir.

A pessoa que fazia BPMN interpretava uma regra de uma maneira e quem fazia UML interpretava de outra.

Depois tínhamos duas versões do mesmo sistema.

**Interviewer:**

Então mudaram o processo?

**Participant:**

Sim.

Continuávamos a ter uma pessoa responsável por fazer o primeiro draft, mas os outros tinham de rever.

E antes de começar outro modelo discutíamos cinco ou dez minutos o que devia transportar do anterior.

**Interviewer:**

Isso era formal ou foi uma coisa que vocês inventaram?

**Participant:**

Nossa.

Não me lembro do professor dizer para fazermos assim.

**Interviewer:**

E funcionou?

**Participant:**

Sim.

Principalmente porque obrigava quem não tinha feito aquele modelo a percebê-lo.

Também ajudou para a defesa.

**Interviewer:**

Na defesa o professor perguntava individualmente?

**Participant:**

Sim, acho que sim.

Não dava para uma pessoa fazer tudo e os outros ficarem calados.

**Interviewer:**

Isso criava stress?

**Participant:**

Um pouco.

Eu sabia explicar o que tínhamos feito, mas nunca gostei muito de não saber qual pergunta vinha a seguir.

**Interviewer:**

E o facto de saberes que ias ter que explicar alterava a qualidade do modelo?

**Participant:**

Sim.

Principalmente simplificar.

Às vezes fazíamos um modelo muito carregado e depois quando tentávamos explicar percebíamos que nem nós conseguíamos seguir aquilo facilmente.

Então dividíamos ou removíamos coisas que não acrescentavam muito.

**Interviewer:**

Interessante, portanto explainability era quase um critério de qualidade.

**Participant:**

Sim.

Não sei se o professor chamava assim, mas na prática sim.

Se três pessoas que fizeram o modelo tinham dificuldade em explicar, provavelmente estava demasiado complicado.

**Interviewer:**

Quando recebias feedback do professor pessoalmente, preferias isso a feedback escrito?

**Participant:**

Sim.

Porque podias perguntar logo "mas porquê?".

Feedback escrito do género "incorrect relationship" não me ajuda muito.

**Interviewer:**

E recebiam feedback escrito?

**Participant:**

Acho que sim, algumas notas.

Mas lembro-me mais das discussões.

**Interviewer:**

E tinhas facilidade em ir falar com o professor?

**Participant:**

Se fosse sozinho ou com o grupo, sim.

Durante a aula inteira era mais difícil.

**Interviewer:**

Por vergonha?

**Participant:**

Um bocado.

Também por não querer fazer uma pergunta básica e interromper a aula.

**Interviewer:**

Mesmo que a dúvida pudesse ser partilhada por outros alunos.

**Participant:**

Sim.

Eu sei que racionalmente não faz muito sentido, mas era assim.

**Interviewer:**

E os professores faziam alguma coisa para facilitar alunos que não queriam falar para a turma?

**Participant:**

Nas práticas eles andavam pela sala às vezes.

Isso ajudava bastante.

Se o professor passa pela tua mesa e pergunta "está tudo bem?", é muito mais fácil mostrar o que estás a fazer do que levantar a mão à frente da turma.

**Interviewer:**

Portanto para ti esse tipo de feedback proativo era melhor.

**Participant:**

Sim, definitivamente.

**Interviewer:**

Quando tinhas um modelo terminado e não havia professor disponível, como decidias se estava bom suficiente?

**Participant:**

Primeiro comparava com o enunciado.

Depois verificava se tinha usado correctamente a notação.

No projecto mostrava aos colegas.

E às vezes aí já usava AI também.

**Interviewer:**

Tinham checklist?

**Participant:**

Não me lembro de uma checklist oficial.

A nossa era quase:

"Está tudo o que o enunciado pede?"

"Há alguma coisa num modelo que contradiz outro?"

"Conseguimos explicar isto?"

**Interviewer:**

E onde entrava a AI nessa checklist?

**Participant:**

Normalmente depois de verificar eu.

Primeiro fazia o modelo e revia.

Depois podia mandar screenshot e contexto e pedir para encontrar inconsistências ou notação estranha.

Depois voltava a verificar as sugestões.

**Interviewer:**

Ou seja não substituía o self-check.

**Participant:**

Não.

Era mais uma segunda opinião.

**Interviewer:**

E se a AI e tu discordassem?

**Participant:**

Ia aos slides ou documentação.

Ou perguntava ao professor.

Principalmente se tivesse impacto no projecto.

**Interviewer:**

E achas que ter AI disponível mudou alguma coisa na forma como participavas nas práticas?

**Participant:**

Sim, provavelmente perguntava ainda menos algumas dúvidas pequenas ao professor.

**Interviewer:**

Isso achas positivo ou negativo?

**Participant:**

Os dois.

Era positivo porque não ficava bloqueado.

Mas às vezes a discussão com o professor ensinava mais.


**Interviewer:**

Portanto idealmente AI devia orientar e não simplesmente entregar a resposta.

**Participant:**

Sim.

Exactamente.

**Interviewer:**

Última pergunta. Se pudesses mudar uma coisa realista sobre a forma como modelação era ensinada, sem inventar uma cadeira completamente nova, o que mudavas?

**Participant:**

Usar o mesmo caso de estudo durante mais tempo.

Começar com requisitos, depois processo, depois UML, talvez SysML, e ir mostrando claramente o que estamos a reutilizar e o que estamos a repensar.

E talvez dar uma maneira mais privada de verificar modelos durante as práticas.

**Interviewer:**

Como assim?

**Participant:**

Pode ser a ferramenta fazer alguma validação ou uma ferramenta com AI.

Não para gerar o modelo.

Só para dizer coisas como:

"esta relação não é válida nesta notação",

"este requisito aparentemente não está coberto",

ou

"tens um elemento no modelo A que contradiz o modelo B".

Para alunos como eu seria útil porque podia verificar algumas dúvidas antes de mostrar à turma ou ao professor.

**Interviewer:**

E achas que isso faria com que produzisses modelos melhores?

**Participant:**

Acho que sim.

Principalmente porque recebia feedback mais cedo.

Se só percebes um problema depois da entrega, podes aprender para a próxima, mas já não melhoras aquele trabalho.

Se percebes enquanto estás a construir ainda consegues corrigir.

**Interviewer:**

Perfeito. Era exactamente esse tipo de informação que eu precisava. Obrigado pelo teu tempo, e caso mais tarde precise esclarecer alguma coisa que tenha ficado ambigua eu entro em contacto.

**Participant:**

Sim, tranquilo.