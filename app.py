#!/usr/bin/env python
# coding: utf-8

# In[1]:



import pandas as pd
import numpy as np
import random
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import plotly.graph_objs as go
import copy


# In[2]:


#Werkversie
app = dash.Dash()
server = app.server
lijst_pijlerz = {'Beleid':
                [('Studentenwelzijn is een strategische prioriteit van ons beleid', 1),
                 ('Studentenwelzijn staat structureel op de agenda bij bestuurlijke overleggen', 1),
                 ('Bij overgangssituaties is er één centraal aanspreekpunt waar studenten/medewerkers \n met vragen over studentenwelzijn terecht kunnen', 2),
                 ('Bij overgangssituaties worden behoeften, wederzijdse rechten en plichten samen met \n de student schriftelijk vastgelegd. ', 2),
                 ('In de organisatie brede richtlijnen voor het ontwerp van curricula is structureel \n aandacht voor studentenwelzijn', 3),
                 ('Het is beleid dat iedere medewerker geregeld aan studenten vraagt hoe het men hen \n gaat en of zij nog ergens hulp bij kunnen gebruiken', 3),
                 ('Het bestuur updatet  medewerkers en studenten jaarlijks over welke (vroege) interventies \n mogelijk zijn en over de route daar naartoe', 4),
                 ('Het bestuur spoort iedere medewerker aan om vroege signalen van studenten(on)welzijn te \n melden of direct te bespreken met de student', 4),
                 ('Er is een begeleidingsstructuur van 1e lijn (bv. slb), 2e lijn (bv. studenten-decaan of –psycholoog) \n en er wordt indien nodig doorverwezen naar externe hulp (bv. GGD)', 5),
                 ('Interne en externe begeleidingsmogelijkheden worden proactief bekend gemaakt aan studenten', 5),
                 ('De school faciliteert medewerkers m.b.t. hun werkdruk zodat zij voldoende ruimte houden \n om studenten te helpen met thema’s op het gebied van studentenwelzijn', 6),
                 ('De school faciliteert medewerkers met trainingen en andere hulpbronnen om hun welzijn te \n bevorderen en om hen beter toe te rusten elkaar en studenten hiermee te helpen', 6),
                 ('Er is een samenwerking met andere organisaties (bv. onderwijs, gemeente), waarin \n initiatieven worden ontplooid ten gunste van (studenten)welzijn', 7),
                 ('Medewerkers krijgen de beschikking over een jaarlijks geüpdatet overzicht van interne \n en externe partners die hulp en ondersteuning bieden', 7),
                 ('Het bestuur monitort jaarlijks effecten van interventies en gebruikt de resultaten om \n deze interventies aan te scherpen', 8),
                 ('De school heeft een lectoraat dat specifiek onderzoek doet naar studentenwelzijn en dat \n in verbinding staat met derden die hier informatie over verzamelen', 8),        
                 ('Studentenwelzijn is een strategische prioriteit van ons beleid', 1),
                 ('Studentenwelzijn staat structureel op de agenda bij bestuurlijke overleggen', 1),
                 ('Bij overgangssituaties is er één centraal aanspreekpunt waar studenten/medewerkers met \n vragen over studentenwelzijn terecht kunnen', 2),
                 ('Bij overgangssituaties worden behoeften, wederzijdse rechten en plichten samen met de \n student schriftelijk vastgelegd', 2),
                 ('In de organisatie brede richtlijnen voor het ontwerp van curricula is structureel aandacht \n voor studentenwelzijn', 3),
                 ('Het is beleid dat iedere medewerker geregeld aan studenten vraagt hoe het men hen gaat en of \n zij nog ergens hulp bij kunnen gebruiken', 3),
                 ('Het bestuur updatet  medewerkers en studenten jaarlijks over welke (vroege) interventies \n mogelijk zijn en over de route daar naartoe', 4),
                 ('Het bestuur spoort iedere medewerker aan om vroege signalen van studenten(on)welzijn te melden \n of direct te bespreken met de student', 4),
                 ('Er is een begeleidingsstructuur van 1e lijn (bv. slb), 2e lijn (bv. studenten-decaan of –psycholoog) \n en er wordt indien nodig doorverwezen naar externe hulp (bv. GGD)', 5),
                 ('Interne en externe begeleidingsmogelijkheden worden proactief bekend gemaakt aan studenten', 5),
                 ('De school faciliteert medewerkers m.b.t. hun werkdruk zodat zij voldoende ruimte houden om \n studenten te helpen met thema’s op het gebied van studentenwelzijn', 6),
                 ('De school faciliteert medewerkers met trainingen en andere hulpbronnen om hun welzijn te \n bevorderen en om hen beter toe te rusten elkaar en studenten hiermee te helpen', 6),
                 ('Er is een samenwerking met andere organisaties (bv. onderwijs, gemeente), waarin initiatieven \/n worden ontplooid ten gunste van (studenten)welzijn', 7),
                 ('Medewerkers krijgen de beschikking over een jaarlijks geüpdatet overzicht van interne en \n externe partners die hulp en ondersteuning bieden', 7),
                 ('Het bestuur monitort jaarlijks effecten van interventies en gebruikt de resultaten om deze \n interventies aan te scherpen', 8),
                 ('De school heeft een lectoraat dat specifiek onderzoek doet naar studentenwelzijn en dat in \n verbinding staat met derden die hier informatie over verzamelen', 8),],
                'Medewerker':
                [('Medewerkers hebben een voorbeeldfunctie in het bespreekbaar maken van (studenten)welzijn', 1),
                 ('Studentenwelzijn staat structureel op de agenda bij overleggen tussen medewerkers', 1),
                 ('Bij aanmelding/ overgang is er aandacht en kennis bij de begeleider voor problemen of signalen rond studentenwelzijn', 2),
                 ('Bij overgangssituaties voert een slb’er het gesprek met de student over behoeften, wederzijdse rechten en plichten en legt dit schriftelijk vast', 2),
                 ('In het ontwerp en de uitvoering van het curriculum is structureel aandacht voor (studenten) welzijn', 3),
                 ('Het is goed gebruik dat iedere medewerker geregeld aan studenten vraagt hoe het met hen gaat en of zij nog ergens hulp bij kunnen gebruiken', 3),
                 ('De slb/lbl houdt kennis over (vroege) interventies op peil en communiceert dat hij/zij studenten hiermee kan helpen', 4),
                 ('Iedere medewerker let op vroege signalen van studenten(on)welzijn en meldt deze bij het bestuur of spreekt er de student direct op aan', 4),
                 ('Medewerkers zijn op de hoogte van en verwijzen indien nodig door naar interne hulp (1e lijn, bv. slb en 2e lijn, bv. studenten-decaan of –psycholoog) of externe hulp (bv. GGD)', 5),
                 ('Medewerkers vertellen zelf proactief over interne en externe begeleidingsmogelijkheden, niet alleen wanneer een student daarom vraagt', 5),
                 ('Medewerkers bespreken in een periodieke intervisie hun werkdruk en hoe voldoende ruimte te houden voor vragen van studenten rond studentenwelzijn.', 6),
                 ('Medewerkers maken gebruik van de trainingen en andere hulpbronnen t.b.v. hun eigen welzijn en zijn daardoor beter in staat elkaar en studenten hiermee te helpen', 6),
                 ('Docenten worden door interne en externe partners geschoold op thema’s die relateren aan studentenwelzijn (bv. stress, zelfmoordpreventie)', 7),
                 ('Medewerkers maken gebruik van een actueel overzicht van interne en externe partners om studenten naartoe te kunnen verwijzen die hulp en ondersteuning nodig hebben', 7),
                 ('Medewerkers evalueren zelfstandig de effecten van hun interventies en gebruiken deze om hun interventies aan te scherpen ', 8),
                 ('Gegevens die door lectoraten en derden worden verzameld op het gebied van (studenten)welzijn worden door medewerkers in het onderwijs geïmplementeerd', 8),
                 ('Medewerkers hebben een voorbeeldfunctie in het bespreekbaar maken van (studenten)welzijn', 1),
                 ('Studentenwelzijn staat structureel op de agenda bij overleggen tussen medewerkers', 1),
                 ('Bij aanmelding/ overgang is er aandacht en kennis bij de begeleider voor problemen of signalen rond studentenwelzijn', 2),
                 ('Bij overgangssituaties voert een slb’er het gesprek met de student over behoeften, wederzijdse rechten en plichten en legt dit schriftelijk vast', 2),
                 ('In het ontwerp en de uitvoering van het curriculum is structureel aandacht voor (studenten) welzijn', 3),
                 ('Het is goed gebruik dat iedere medewerker geregeld aan studenten vraagt hoe het met hen gaat en of zij nog ergens hulp bij kunnen gebruiken', 3),
                 ('De slb/lbl houdt kennis over (vroege) interventies op peil en communiceert dat hij/zij studenten hiermee kan helpen', 4),
                 ('Iedere medewerker let op vroege signalen van studenten(on)welzijn en meldt deze bij het bestuur of spreekt er de student direct op aan', 4),
                 ('Medewerkers zijn op de hoogte van en verwijzen indien nodig door naar interne hulp (1e lijn, bv. slb en 2e lijn, bv. studenten-decaan of –psycholoog) of externe hulp (bv. GGD)', 5),
                 ('Medewerkers vertellen zelf proactief over interne en externe begeleidingsmogelijkheden, niet alleen wanneer een student daarom vraagt', 5),
                 ('Medewerkers bespreken in een periodieke intervisie hun werkdruk en hoe voldoende ruimte te houden voor vragen van studenten rond studentenwelzijn', 6),
                 ('Medewerkers maken gebruik van de trainingen en andere hulpbronnen t.b.v. hun eigen welzijn en zijn daardoor beter in staat elkaar en studenten hiermee te helpen', 6),
                 ('Docenten worden door interne en externe partners geschoold op thema’s die relateren aan studentenwelzijn (bv. stress, zelfmoordpreventie)', 7),
                 ('Medewerkers maken gebruik van een actueel overzicht van interne en externe partners om studenten naartoe te kunnen verwijzen die hulp en ondersteuning nodig hebben', 7),
                 ('Medewerkers evalueren zelfstandig de effecten van hun interventies en gebruiken deze om hun interventies aan te scherpen', 8),
                 ('Gegevens die door lectoraten en derden worden verzameld op het gebied van (studenten)welzijn worden door medewerkers in het onderwijs geïmplementeerd', 8)],
                 'Studenten':
                [('Medezeggenschap van studenten omtrent studentenwelzijn is aantoonbaar geregeld', 1),
                 ('Studentenwelzijn staat structureel op de agenda bij overleggen bij studentenvertegenwoordigingen, studieverenigingen, enz', 1),
                 ('Bij de overgang krijgt iedere nieuwe student een buddy toegewezen die aandacht heeft voor het welzijn van de student', 2),
                 ('Bij overgangssituaties is het voor een student laagdrempelig om in gesprek met de slb’er te spreken over behoeften, wederzijdse rechten en plichten', 2),
                 ('In de uitvoering van het curriculum is structureel aandacht voor (studenten)welzijn', 3),
                 ('Studenten wordt regelmatig gevraagd (door slb’er maar ook door docenten of conciërge) hoe het met hen gaat en of zij nog ergens hulp bij kunnen gebruiken', 3),
                 ('Het is voor studenten duidelijk bij wie zij terecht kunnen met (vroege) signalen over (studenten)welzijn', 4),
                 ('Het is geaccepteerd gebruik dat wanneer een student niet goed in zijn/haar vel zit, hij/zij hierover kan worden aangesproken door een medewerker', 4),
                 ('De begeleidingsstructuur van 1e lijn (bv. slb), 2e lijn (bv. studentendecaan of –psycholoog) en doorverwijzing naar externe hulp (b.v. GGD) is voldoende bekend en toegankelijk voor studenten', 5),
                 ('Studenten krijgen regelmatig informatie over interne en externe begeleidingsmogelijkheden', 5),
                 ('Studenten hebben het idee dat er altijd ruimte is om problemen rond studentenwelzijn te bespreken met medewerkers en dat werkdruk van medewerkers dit niet in de weg staat', 6),
                 ('Studenten herkennen dat medewerkers zich ontwikkelen op het terrein van (studenten)welzijn en voelen zich daardoor beter gesteund/geholpen door medewerkers', 6),
                 ('Het is voor studenten herkenbaar met welke andere organisaties hun school samenwerkt en zij kunnen hier laagdrempelig naar worden doorverwezen', 7),
                 ('Studenten kunnen gebruik maken van een actueel overzicht van interne en externe partners die hulp en ondersteuning bieden', 7),
                 ('Jaarlijks wordt een onderzoek gehouden onder studenten naar (studenten) welzijn en het aanbod daar rondom, om evt. problemen te detecteren en het aanbod te verbeteren', 8),
                 ('Studenten worden met enige regelmaat geïnformeerd over nieuwe inzichten die het lectoraat (al dan niet via derden) heeft opgedaan over studentenwelzijn', 8),
                 ('Medezeggenschap van studenten omtrent studentenwelzijn is aantoonbaar geregeld', 1),
                 ('Studentenwelzijn staat structureel op de agenda bij overleggen bij studentenvertegenwoordigingen, studieverenigingen, enz', 1),
                 ('Bij de overgang krijgt iedere nieuwe student een buddy toegewezen die aandacht heeft voor het welzijn van de student', 2),
                 ('Bij overgangssituaties is het voor een student laagdrempelig om in gesprek met de slb’er te spreken over behoeften, wederzijdse rechten en plichten', 2),
                 ('In de uitvoering van het curriculum is structureel aandacht voor (studenten)welzijn', 3),
                 ('Studenten wordt regelmatig gevraagd (door slb’er maar ook door docenten of conciërge) hoe het met hen gaat en of zij nog ergens hulp bij kunnen gebruiken', 3),
                 ('Het is voor studenten duidelijk bij wie zij terecht kunnen met (vroege) signalen over (studenten)welzijn', 4),
                 ('Het is geaccepteerd gebruik dat wanneer een student niet goed in zijn/haar vel zit, hij/zij hierover kan worden aangesproken door een medewerker', 4),
                 ('De begeleidingsstructuur van 1e lijn (bv. slb), 2e lijn (bv. studentendecaan of –psycholoog) en doorverwijzing naar externe hulp (b.v. GGD) is voldoende bekend en toegankelijk voor studenten', 5),
                 ('Studenten krijgen regelmatig informatie over interne en externe begeleidingsmogelijkheden', 5),
                 ('Studenten hebben het idee dat er altijd ruimte is om problemen rond studentenwelzijn te bespreken met medewerkers en dat werkdruk van medewerkers dit niet in de weg staat', 6),
                 ('Studenten herkennen dat medewerkers zich ontwikkelen op het terrein van (studenten)welzijn en voelen zich daardoor beter gesteund/geholpen door medewerkers', 6),
                 ('Het is voor studenten herkenbaar met welke andere organisaties hun school samenwerkt en zij kunnen hier laagdrempelig naar worden doorverwezen', 7),
                 ('Studenten kunnen gebruik maken van een actueel overzicht van interne en externe partners die hulp en ondersteuning bieden', 7),
                 ('Jaarlijks wordt een onderzoek gehouden onder studenten naar (studenten) welzijn en het aanbod daar rondom, om evt. problemen te detecteren en het aanbod te verbeteren', 8),
                 ('Studenten worden met enige regelmaat geïnformeerd over nieuwe inzichten die het lectoraat (al dan niet via derden) heeft opgedaan over studentenwelzijn', 8)]}


old_database = {'Haagse Hoge school' : {'Beleid': {'Scores' : [1,4,0,1,3,1,4,2], 'Aantal': 10}, 
               'Medewerker': {'Scores' : [4,4,3,3,0,0,0,2], 'Aantal': 15},
               'Studenten': {'Scores' : [0,0,4,4,4,4,0,0], 'Aantal': 6}},
                'Hoge school voor de kunsten' : {'Beleid': {'Scores' : [4,1,1,3,1,4,2,0], 'Aantal': 6}, 
               'Medewerker': {'Scores' : [1,1,1,3,2,4,4,0], 'Aantal': 3},
               'Studenten': {'Scores' : [1,1,4,4,4,2,0,0], 'Aantal': 8}},
                'TU Delft' : {'Beleid': {'Scores' : [2,2,2,2,2,2,2,2], 'Aantal': 2}, 
               'Medewerker': {'Scores' : [3,3,3,3,4,0,0,0], 'Aantal': 22},
               'Studenten': {'Scores' : [1,3,4,2,2,1,1,1], 'Aantal': 68}}
               }

r = [0,0,0,0,0,0,0,0]
app.layout = html.Div(
    [   html.H1('Aan de slag met het Kompas Studentenwelzijn',style={'backgroundColor': '#b6dbbf'}),
        html.P('Ben je beleidsbepaler, onderwijsprofessional of student? En ben je op zoek'),
        html.P('naar een aanpak voor een gedeeld beeld en gezamenlijke taal voor het bevorderen van studentenwelzijn?'),
        html.P('Ga dan direct aan de slag! Je deelname is volledig anoniem.'),

        html.H3('Selecteer de doelgroep die op jou van toepassing is.'),
        
        html.Div([
        html.Div([
        dcc.Dropdown(
            id='naam',
            options=[{'label':nametitle, 'value':name} for nametitle,name in 
                     zip(['Beleidsbepaler', 'Medewerker', 'Studenten'],
                         ['Beleid', 'Medewerker', 'Studenten']) ],style={'display': 'inline-block','width': '50%'})
        
  
        ]),

        
        ]),
     
        html.Div(html.H1('Stellingen',style={ 'backgroundColor': '#b6dbbf'})),
        html.Div(html.P('Nadat je de doelgroep hebt geselecteerd worden hieronder 16 keer twee stellingen gegeven. Kies steeds de stellingen waaraan jij prioriteit geeft.')),
        html.Div(html.P('Er zijn geen goede of foute antwoorden, het gaat om jouw beleving.')),
        html.H3(id = 'tekst',style={  'textAlign': 'right'}),
     
        html.Div(dash_table.DataTable(
        id='table',
        columns=[
            {"name": i, "id": i} for i in sorted(['Antwoord', 'Stelling'])
        ] ,style_cell_conditional=[
                {
                    'if': {'column_id': 'Stelling'},
                    'textAlign': 'left'
                },{
                    'if': {'column_id': 'Antwoord'},
                    'textAlign': 'center'
                },
            ]), style={'width': '49%','backgroundColor': '#b6dbbf'}),
     
        html.H3('Kies A of B met de stelling waaraan jij prioriteit geeft:'),
     
        html.Div(
            
        html.Thead([
            html.Tr(html.Th('', colSpan="2")),
            html.Tr([
                html.Th(html.Button('Kies A', id='knopA', n_clicks_timestamp='0')),
                html.Th(html.Button('Kies B', id='knopB', n_clicks_timestamp='0')),
                html.Th(html.Button('Herstart', id='herstart', n_clicks_timestamp='0'))
            ])]
            
        )),
        html.Div(html.H1('Vergelijking',style={'backgroundColor': '#b6dbbf'})),
        
        html.Div(
        html.H3('Vergelijk je gegevens met die van anderen: '),),
        html.P('Deze functie is ter illustratie en geeft fictieve resultaten weer.'),
        html.Div(html.H3('Doelgroep:' )),
        html.Div([dcc.Dropdown(id=  'kies_school',options=[{'label':nametitle, 'value':name} for nametitle,name in 
                     zip(['Instelling 1', 'Instelling 2', 'Instelling 3'],
                         ['Haagse Hoge school', 'Hoge school voor de kunsten', 'TU Delft']) ],value = 'TU Delft', style={'display': 'inline-block','width': '66%'} )]),
        html.Div(html.H3('Onderwijsinstelling:')),
        html.Div([dcc.Dropdown(id=  'kies_groep',options=[{'label':nametitle, 'value':name} for nametitle,name in 
                     zip(['Beleid', 'Medewerker', 'Studenten'],
                         ['Beleid', 'Medewerker', 'Studenten']) ],value = 'Studenten',style={'display': 'inline-block','width': '66%'} )])
        ,
        html.Div([dcc.Store(id='waarden',storage_type='memory'),]),
        html.Div([dcc.Store(id='dataone',storage_type='memory'),]),
        html.Div([dcc.Store(id='gekozen',storage_type='memory'),]),
        html.Div([dcc.Store(id='nummer_stor',storage_type='memory'),]),
        html.Div(dcc.Graph(id = 'Chart'))])



@app.callback(
    [dash.dependencies.Output('table', 'data'),
     dash.dependencies.Output('waarden', 'data'),
    dash.dependencies.Output('dataone', 'data'),
    dash.dependencies.Output('nummer_stor', 'data'),
    dash.dependencies.Output('tekst', 'children'),
    dash.dependencies.Output('gekozen', 'data')],
    [dash.dependencies.Input('naam', 'value'), 
     dash.dependencies.Input('knopA', 'n_clicks_timestamp'),
     dash.dependencies.Input('knopB', 'n_clicks_timestamp'), 
    ], [dash.dependencies.State('waarden', 'data'),
       dash.dependencies.State('table', 'data'),
       dash.dependencies.State('dataone', 'data'), 
       dash.dependencies.State('nummer_stor', 'data'),
       dash.dependencies.State('gekozen', 'data')])
def update_table(groep, vragenn, vragennn,datak, datafr, lijst_pijlers, nummer, huidige_groep):
    gekozen_groep = groep
    if gekozen_groep != huidige_groep:
        datak = [0,0,0,0,0,0,0,0]
        lijst_pijlers = copy.deepcopy(lijst_pijlerz)
        nummer = 0
    while nummer is None:
        nummer = 0
    while lijst_pijlers is None:
        lijst_pijlers = copy.deepcopy(lijst_pijlerz)
        datak = [0,0,0,0,0,0,0,0]
    while datak is None:
        lijst_pijlers = copy.deepcopy(lijst_pijlerz)
        datak = [0,0,0,0,0,0,0,0]
    if len(lijst_pijlers[groep]) == 0 and np.sum(datak) == 15:
        if int(vragenn) > int(vragennn):
            datak[int(datafr[0]['Test'])-1] = datak[int(datafr[0]['Test'])-1] + 1
        if int(vragennn) > int(vragenn):
            datak[int(datafr[1]['Test'])-1] = datak[int(datafr[1]['Test'])-1] + 1 
        df = [{'Antwoord': '', 'Stelling': 'Bedankt voor het invullen!'}, {'Antwoord': '', 'Stelling': 'De test is klaar!'}]
        nummer_output = nummer
        tekst_output = 'Stelling ' + str(nummer_output) + "/16"
        return df, datak, lijst_pijlers, nummer_output, tekst_output, gekozen_groep
    uno = random.randint(0,len(lijst_pijlers[groep])-1)
    uno_PL = lijst_pijlers[groep][uno][1]
    uno_Stel = lijst_pijlers[groep][uno][0]
    lijst_pijlers[groep].pop(uno)
    duo= random.randint(0,len(lijst_pijlers[groep])-1)
    duo_PL = lijst_pijlers[groep][duo][1]
    duo_Stel = lijst_pijlers[groep][duo][0]
    while uno_PL == duo_PL or uno_Stel == duo_Stel:
        duo = random.randint(0,len(lijst_pijlers[groep])-1)
        duo_PL = lijst_pijlers[groep][duo][1]
        duo_Stel = lijst_pijlers[groep][duo][0]
    lijst_pijlers[groep].pop(duo)
    df = [{'Antwoord': 'A', 'Stelling': uno_Stel, 'Test' : uno_PL}, {'Antwoord': 'B', 'Stelling': duo_Stel, 'Test' : duo_PL}]
    if len(lijst_pijlers[groep]) == 30:
        datak = [0,0,0,0,0,0,0,0]
    if gekozen_groep == huidige_groep:
        if int(vragenn) > int(vragennn):
            datak[int(datafr[0]['Test'])-1] = datak[int(datafr[0]['Test'])-1] + 1
        if int(vragennn) > int(vragenn):
            datak[int(datafr[1]['Test'])-1] = datak[int(datafr[1]['Test'])-1] + 1 
    if gekozen_groep != huidige_groep:
        datak = [0,0,0,0,0,0,0,0]
    
    nummer_output = nummer + 1
    tekst_output = 'Stelling ' + str(nummer_output) + "/16"
    return df, datak, lijst_pijlers, nummer_output, tekst_output, gekozen_groep


@app.callback(
    dash.dependencies.Output('Chart', 'figure'),
    [dash.dependencies.Input('naam', 'value'),
    dash.dependencies.Input('kies_school', 'value'),
    dash.dependencies.Input('kies_groep', 'value'),
    dash.dependencies.Input('waarden', 'data')])
def update_figure(groep, school, groepp, infor):
    piedata = go.Scatterpolar(name = 'Eigen score',
  r=infor,
  theta=['Leiderschap/bestuurlijke visie', 'Overgang school-school','Preventie', 'Vroege interventie', 
                 'Begeleiding', 'Medewerkers', 'Partners-extern netwerk', 'Data en onderzoek'],
  fill='toself'
)
    piedata_two = go.Scatterpolar(name = 'Vergelijkingsscore',
  r=old_database[school][groepp]['Scores'],
  theta=['Leiderschap/bestuurlijke visie', 'Overgang school-school','Preventie', 'Vroege interventie', 
                 'Begeleiding', 'Medewerkers', 'Partners-extern netwerk', 'Data en onderzoek'],
  fill='toself'
)
    layout = go.Layout( title='Vergelijking', )
    return {'data': [piedata, piedata_two], 'layout' : layout}


# In[3]:


if __name__ == '__main__':
    app.run_server()
