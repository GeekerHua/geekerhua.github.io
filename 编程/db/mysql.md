mysql 编码修改



1. 查看数据库编码

   ```mysq
   show variables like '%char%'
   ```

2. 临时修改数据库编码

   ```mysql
   SET character_set_client = utf8;
   SET character_set_connection = utf8;
   SET character_set_database = utf8;
   SET character_set_results = utf8;
   SET character_set_server = utf8;
   ```

3. 查看数据表编码

   ```mysql
   show create table score;
   ```

4. 修改数据表编码

   ```mysql
   alter table score default character set utf8;
   ```

5. 修改数据列编码

   ```mysql
    alter table score change score score varchar(50) character utf8;
   ```


## 优化

1. 删除整张表数据, 大批量删除

   使用 trunct, 不是delete，delete会产生大量的日志

2. 禁止3张表以上的关联，关联字段数据类型绝对一致，要有索引

3. 分页优化

   ```sql
   select t2.* from (select id from TASK ) t1 buyer t2 where t1.id=t2.id;
   ```


