from database.DB_connect import DBConnect


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getYears():
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct c.`year` 
                    from contiguity c 
                    order by year asc"""

        cursor.execute(query)

        for row in cursor:
            results.append(row["year"])

        cursor.close()
        conn.close()
        return results

    def getNodes(anno):
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT DISTINCT c.CCode, c.StateAbb, c.StateNme
                    FROM country c
                    JOIN (
                        SELECT state1no AS codice_stato
                        FROM contiguity
                        WHERE year <= %s
                    
                        UNION
                    
                        SELECT state2no AS codice_stato
                        FROM contiguity
                        WHERE year <= %s
                    ) AS stati_presenti
                    ON c.CCode = stati_presenti.codice_stato
                    ORDER BY c.StateNme;"""

        cursor.execute(query, (anno, anno,))

        results = cursor.fetchall()

        cursor.close()
        conn.close()
        return results

    @staticmethod
    def get_archi(anno):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        query = """
                SELECT DISTINCT state1no, state2no
                FROM contiguity
                WHERE year <= %s
                  AND conttype = 1
            """

        cursor.execute(query, (anno,))
        result = cursor.fetchall()

        cursor.close()
        conn.close()

        return result