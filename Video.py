import datetime
import db

class Video:
    def __init__(self, url, local_path, category, subcategory, duration,
                 title, description, is_downloaded=False, is_merged=False, last_merged_at=datetime.datetime.min,
                 is_short=False):
        self.url = url
        self.local_path = local_path,
        self.is_downloaded = is_downloaded
        self.is_merged = is_merged
        self.last_merged_at = last_merged_at
        self.category = category
        self.subcategory = subcategory,
        self.duration = duration,
        self.title = title,
        self.description = description,
        self.is_short = is_short

    def __str__(self):
        return self.__dict__

    def insert_video(self):
        query = """
                insert into videos 
                (url,local_path,is_downloaded,is_merged,last_merged_at,category,subcategory
                duration,title,description,is_short) values (%s, %s, %s, %s, %s, %s, %s)
                """

        cur = db.get_new_connection()
        try:
            error = cur.execute(query, (self.url, self.local_path, self.is_downloaded, self.is_merged, self.last_merged_at,
                            self.category, self.subcategory, self.duration, self.title, self.description, self.is_short))
        except Exception as e:
            db.print_psycopg2_exception(e)
            raise IOError("Cannot insert video {}".format(self))

    def save(self):
        query = """
        update videos 
        set url = %s, set local_path = %s, set is_downloaded = %s, set is_merged = %s, set last_merged_at = %s, 
        set category = %s, set subcategory = %s, set duration = %s, set title = %s, set description = %s, set is_short = %s, 
        """
        cur = db.get_new_connection()
        try:
            error = cur.execute(query,
                                (self.url, self.local_path, self.is_downloaded, self.is_merged, self.last_merged_at,
                                 self.category, self.subcategory, self.duration, self.title, self.description,
                                 self.is_short))
        except Exception as e:
            db.print_psycopg2_exception(e)
            raise IOError("Cannot update video {}".format(self))



