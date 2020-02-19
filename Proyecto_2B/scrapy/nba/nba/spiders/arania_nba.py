import scrapy
import pandas as pd
import numpy as np
class AraniaNBA(scrapy.Spider):
    name = 'nba'
    path_archivos = "C://Users//Andres//Desktop//PYTHON//py-pantoja-pino-andres-sebastian//Proyecto_2B//archivos//"
    standings_columns = ['Equipo', 'Victorias', 'Derrotas']
    playoff_prob_columns = ['Equipo', 'Probabilidad']
    mvp_prob_columns = ['Jugador', 'Probabilidad']
    partidos_columns = ['Visitantes', 'Locales']
    leaders_columns = ['Estadistica', 'Puntaje']
    total_standings_columns = ['Equipo', 'Porcentajes']
    stats_columns = ['TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']
    equipos_este = None
    equipos_oeste = None
    url_total_standings = 'https://www.basketball-reference.com/leagues/NBA_2020_standings.html'
    urls = [
        'https://www.basketball-reference.com/'
    ]

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url)

    def parse(self, response):
        self.equipos_este = response.xpath("//table[@id='confs_standings_E']/tbody/tr/th[@data-stat='team_name']/a/text()").extract()
        victorias_este = response.xpath("//table[@id='confs_standings_E']/tbody/tr/td[@data-stat='wins']/text()").extract()
        derrotas_este = response.xpath("//table[@id='confs_standings_E']/tbody/tr/td[@data-stat='losses']/text()").extract()

        self.equipos_oeste = response.xpath("//table[@id='confs_standings_W']/tbody/tr/th[@data-stat='team_name']/a/text()").extract()
        victorias_oeste = response.xpath("//table[@id='confs_standings_W']/tbody/tr/td[@data-stat='wins']/text()").extract()
        derrotas_oeste = response.xpath("//table[@id='confs_standings_W']/tbody/tr/td[@data-stat='losses']/text()").extract()
        este = np.column_stack((np.array(self.equipos_este), np.array(victorias_este)))
        este = np.column_stack((este, np.array(derrotas_este)))
        
        df_este = pd.DataFrame(este, columns = self.standings_columns)
        df_este.to_csv(self.path_archivos + 'standings_east.csv', index = False, columns = self.standings_columns)
        oeste = np.column_stack((np.array(self.equipos_oeste), np.array(victorias_oeste)))
        oeste = np.column_stack((oeste, np.array(derrotas_oeste)))

        visitas = response.xpath("//div[@id='scheduled-games']/div[2]/table[1]/tr/td/small/a[1]/text()").extract()
        locales = response.xpath("//div[@id='scheduled-games']/div[2]/table[1]/tr/td/small/a[2]/text()").extract()
        partidos = este = np.column_stack((np.array(visitas), np.array(locales)))
        df_partidas =  df_este = pd.DataFrame(partidos, columns = self.partidos_columns)
        df_este.to_csv(self.path_archivos + 'matches.csv', index = False, columns = self.partidos_columns)
        
        
        df_oeste = pd.DataFrame(oeste, columns = self.standings_columns)
        df_oeste.to_csv(self.path_archivos + 'standings_west.csv', index = False, columns = self.standings_columns)

        link_playoff_probability = self.generate_playoff_prob_link(response)                
        yield scrapy.Request(
                url = link_playoff_probability,
                callback = self.parse_playoff_prob)
        link_mvp_probability = self.generate_mvp_prob_link(response)
        yield scrapy.Request(
                url = link_mvp_probability,
                callback = self.parse_mvp_prob)

        link_leaders = self.generate_leaders_link(response)
        yield scrapy.Request(
                url = link_leaders,
                callback = self.parse_leaders)

        yield scrapy.Request(
                url = self.url_total_standings,
                callback = self.parse_total_standings)

    def parse_total_standings(self, response):
        teams = response.xpath("//div[contains(@class,'table_outer_container')]/div[1]/table[1]/tbody/tr/th/a/text()").extract()[:30] 
        win_loss_ratio = response.xpath("//div[contains(@class,'table_outer_container')]/div[1]/table[1]/tbody/tr/td[@data-stat='win_loss_pct']/text()").extract()[:30] 
        win_loss_ratio =  [float(x) for x in win_loss_ratio]
        total_standings = np.column_stack((np.array(teams), np.array(win_loss_ratio)))
        df_total_standings = pd.DataFrame(total_standings, columns = self.total_standings_columns)
        df_total_standings.to_csv(self.path_archivos + 'total_standings.csv', index = False, columns = self.total_standings_columns)


    def parse_playoff_prob(self, response):
        prob_este = response.xpath("//table[@id='projected_standings_e']/tbody/tr/td[@data-stat='prob_playoffs']/text()").extract()
        prob_oeste = response.xpath("//table[@id='projected_standings_w']/tbody/tr/td[@data-stat='prob_playoffs']/text()").extract()
        prob_win_finals_este = response.xpath("//table[@id='projected_standings_e']/tbody/tr/td[@data-stat='prob_win_finals']/text()").extract()
        prob_win_finals_oeste = response.xpath("//table[@id='projected_standings_w']/tbody/tr/td[@data-stat='prob_win_finals']/text()").extract()
        prob_este =  [float(x[:-1]) for x in prob_este]
        prob_oeste =  [float(x[:-1]) for x in prob_oeste]
        prob_win_finals_este =  [float(x[:-1]) for x in prob_win_finals_este]
        prob_win_finals_oeste =  [float(x[:-1]) for x in prob_win_finals_oeste]

        for i in range((len(self.equipos_este) - len(prob_este))):
            prob_este.append(0)
        for i in range((len(self.equipos_oeste) - len(prob_oeste))):
            prob_oeste.append(0)

        
        for i in range((len(self.equipos_este) - len(prob_win_finals_este))):
            prob_win_finals_este.append(0)
        for i in range((len(self.equipos_oeste) - len(prob_win_finals_oeste))):
            prob_win_finals_oeste.append(0)

        este = np.column_stack((np.array(self.equipos_este), np.array(prob_este)))
        oeste = np.column_stack((np.array(self.equipos_oeste), np.array(prob_oeste)))

        df_este = pd.DataFrame(este, columns = self.playoff_prob_columns)
        df_este.to_csv(self.path_archivos + 'playoffs_probs_east.csv', index = False, columns = self.playoff_prob_columns)
        df_oeste = pd.DataFrame(oeste, columns = self.playoff_prob_columns)
        df_oeste.to_csv(self.path_archivos + 'playoffs_probs_west.csv', index = False, columns = self.playoff_prob_columns)

        full_teams = self.equipos_este.copy()
        full_teams.extend(self.equipos_oeste)
        full_prob_win_finals = prob_win_finals_este.copy()
        full_prob_win_finals.extend(prob_win_finals_oeste)
        prob_win = np.column_stack((np.array(full_teams), np.array(full_prob_win_finals)))
        df_win_finals = pd.DataFrame(prob_win, columns= self.playoff_prob_columns)
        df_win_finals.to_csv(self.path_archivos + 'win_probs.csv', index= False, columns= self.playoff_prob_columns)

    def parse_leaders(self, response):
        stat = response.xpath("//div[@id='meta']/div/p/strong/text()").extract()
        players = response.xpath("//div[@id='meta']/div/p/a/text()").extract()[2:]
        number = response.xpath("//div[@id='meta']/div[2]/p/text()").extract()[1::2]
        number =  [float(x[2:-1]) for x in number]
        final_stat = []
        for i in range(len(stat)):
            final_stat.append(stat[i] + " " + players[i])

        leaders = np.column_stack((np.array(final_stat), np.array(number)))
        df_leaders = pd.DataFrame(leaders, columns = self.leaders_columns)
        df_leaders.to_csv(self.path_archivos + 'leaders.csv', index= False, columns= self.leaders_columns)

    def parse_mvp_prob(self, response):
        players = response.xpath("//table[@id='players']/tbody/tr/td[@data-stat='player']/a/text()").extract()
        mvp_probs = response.xpath("//table[@id='players']/tbody/tr/td[@data-stat='value']/text()").extract()
        mvp_probs =  [float(x[:-1]) for x in mvp_probs]

        mvp_probabilities = np.column_stack((np.array(players), np.array(mvp_probs)))
        df_mvp_probs = pd.DataFrame(mvp_probabilities, columns = self.mvp_prob_columns)
        df_mvp_probs.to_csv(self.path_archivos + 'mvp_probs.csv', index = False, columns = self.mvp_prob_columns)

        
        link_mvp_1_probability = self.generate_mvp_prob_1_link(response)
        
        yield scrapy.Request(
                url = link_mvp_1_probability,
                callback = self.parse_fisrt_mvp_prob)
        
    def parse_fisrt_mvp_prob(self, response):
        stats_2019 = response.xpath("//table[@id='per_game']/tbody/tr[@id='per_game.2019']/td/text()").extract()[-7:]
        stats_2020 = response.xpath("//table[@id='per_game']/tbody/tr[@id='per_game.2020']/td/text()").extract()[-7:]
        stats_2019 =  [float(x) for x in stats_2019]
        stats_2020 =  [float(x) for x in stats_2020]
        print(stats_2019)
        print(stats_2020)
        stats_mvp = np.vstack((stats_2019, stats_2020))
        print(" ---------------------------------- ")
        print(stats_mvp)
        df_stats_mvp = pd.DataFrame(stats_mvp, columns = self.stats_columns)
        df_stats_mvp.to_csv(self.path_archivos + 'mvp_stats.csv', index = False, columns = self.stats_columns)



    def generate_mvp_prob_1_link(self, response):
        aditional_info = response.xpath("//table[@id='players']/tbody/tr[1]/td[@data-stat='player']/a/@href").extract()
        return self.urls[0] + aditional_info[0]


    def generate_playoff_prob_link(self, response):
        aditional_info = response.xpath("//div[@id='current']/div/h3[2]/a/@href").extract()
        return self.urls[0] + aditional_info[0]
        


    def generate_mvp_prob_link(self, response):
        aditional_info = response.xpath("//div[@id='current']/div/h3[3]/a/@href").extract()
        return self.urls[0] + aditional_info[0]

    def generate_leaders_link(self, response):
        aditional_info = response.xpath("//div[@id='leaders']/div[1]/ul[1]/li[1]/a/@href").extract()
        return self.urls[0] + aditional_info[0]