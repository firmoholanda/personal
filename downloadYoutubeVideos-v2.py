from subprocess import call


cmdString = 'youtube-dl -v -i ' \
            '--rate-limit 2M ' \
            '--format "bestvideo+bestaudio[ext=m4a]/bestvideo+bestaudio/best" --merge-output-format mp4 ' \
            '--min-views 1000 ' \
            '--output "c:\\temp\\videos\\%(title)s.%(ext)s" ' \
            'ytsearch10:"ufo footage" '

call(cmdString, shell=True)