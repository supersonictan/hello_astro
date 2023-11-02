# hello_astro
astro automatic

### Set CVM
1. sudo yum install git
2. ssh-keygen -t rsa -b 4096 -C "376079374@qq.com"
3. 复制公钥到git：~/.ssh/id_rsa.pub
4. wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
5. bash Miniconda3-latest-Linux-x86_64.sh
6. conda install beautifulsoup4
7. conda install requests
8. 用于rz和sz命令：sudo yum install lrzsz
9. pip install web.py
10. conda install -c conda-forge jieba 用于cpca 地址解析
11. conda install -c conda-forge cpca
12. 更新conda源
    - conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
    - conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/


### Update——2023年10月17日
 - 增加 knowledge_web.ini 文件
 - TODO：
   + [ ] 增加 http 抓取结果的 cache
   + [x] 命主星落宫的解析
   + [x] 婚神落宫的解析
   + [x] 初等学业、高等学业解析
   + [ ] 增加性格解析（星性合像等）
   - 日返、月返推运
     - [ ] 工作：跳槽、升职加薪
     - [ ] 财富：财运起伏
       - 健康：健康如何，不好时候说明疾病
       - 恋爱：开始一段恋情、分手、吵架
       - 婚姻：离婚、结婚、吵架
       - 出国旅游：
       - 
   - 根据生日+重大事件做生时校准
