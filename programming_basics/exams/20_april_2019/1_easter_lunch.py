easter_bread = int(input())
bark_eggs = int(input())
kg_cookies = int(input())

easter_bread_price = easter_bread * 3.20
bark_eggs_price = bark_eggs * 4.35
cookies_price = kg_cookies * 5.40
egg_paint_price = bark_eggs * 12 * 0.15

total = easter_bread_price + bark_eggs_price + cookies_price + egg_paint_price

print(f'{total:.2f}')
