import re, os
os.chdir('/tmp/firefly-build')

def edit(path, repls):
    c = open(path, encoding='utf-8').read()
    for old, new, note in repls:
        if old not in c:
            print(f'[WARN] {path}: 未找到 {note}')
        else:
            c = c.replace(old, new, 1)
            print(f'[OK] {note}')
    open(path, 'w', encoding='utf-8').write(c)

# 1. 评论区 giscus
e = '/tmp/firefly-build/src/config/commentConfig.ts'
c = open(e, encoding='utf-8').read()
c = c.replace('type: "none"', 'type: "giscus"', 1)
c = c.replace('repo: "CuteLeaf/Firefly"', 'repo: "hzp20070123-pixel/Firefly"', 1)
c = c.replace('repoId: "R_kgD2gfdFGd"', 'repoId: "R_kgDOTrHrXQ"', 1)
c = c.replace('categoryId: "DIC_kwDOKy9HOc4CegmW"', 'categoryId: "DIC_kwDOTrHrXc4DChgL"', 1)
open(e, 'w', encoding='utf-8').write(c)
print('[OK] 评论区已切换为giscus(你的仓库)')

# 2. 樱花特效
edit('/tmp/firefly-build/src/config/effectsConfig.ts', [
    ('// 是否启用樱花特效\n\tenable: false,', '// 是否启用樱花特效\n\tenable: true,', '樱花特效开启'),
])

# 3. 页脚注入
edit('/tmp/firefly-build/src/config/footerConfig.ts', [
    ('\tenable: false,', '\tenable: true,', '页脚注入开启'),
])
open('/tmp/firefly-build/src/config/FooterConfig.html', 'w', encoding='utf-8').write('<p style="text-align:center;">© 2026 HZP\'s Blog · Powered by <a href="https://astro.build" target="_blank">Astro</a> & <a href="https://pages.cloudflare.com" target="_blank">Cloudflare Pages</a></p>')
print('[OK] 页脚内容已写入')

# 4. 代码块语言Logo
edit('/tmp/firefly-build/src/config/expressiveCodeConfig.ts', [
    ('// 语言Logo插件配置（在代码块右下角显示语言图标）\n\tpluginLanguageLogo: {\n\t\t// 是否启用语言Logo插件\n\t\tenable: false,', '// 语言Logo插件配置（在代码块右下角显示语言图标）\n\tpluginLanguageLogo: {\n\t\t// 是否启用语言Logo插件\n\t\tenable: true,', '代码块语言Logo开启'),
])

# 5. 看板娘(Spine + Live2D)
edit('/tmp/firefly-build/src/config/pioConfig.ts', [
    ('// Spine 看板娘开关\n\tenable: false,', '// Spine 看板娘开关\n\tenable: true,', 'Spine看板娘开启'),
    ('live2dWidgetConfig: Live2DWidgetConfig = {\n\tenable: false,', 'live2dWidgetConfig: Live2DWidgetConfig = {\n\tenable: true,', 'Live2D看板娘开启'),
])

# 6. 随机封面图
edit('/tmp/firefly-build/src/config/coverImageConfig.ts', [
    ('// 随机封面图功能开关\n\t\tenable: false,', '// 随机封面图功能开关\n\t\tenable: true,', '随机封面图开启'),
])

# 7. 壁纸轮播
edit('/tmp/firefly-build/src/config/backgroundWallpaper.ts', [
    ('// 是否启用壁纸轮播；关闭时保持每次刷新随机显示一张\n\t\t\tenable: false,', '// 是否启用壁纸轮播；关闭时保持每次刷新随机显示一张\n\t\t\tenable: true,', '壁纸轮播开启'),
])

print('\n=== 全部开关处理完毕 ===')
