这个项目的具体要求是编写一个 Python 程序来模拟咖啡自动售货机的软件。咖啡售卖过程应包括以下操作：

1. 程序以可用饮料的菜单开始等待选择。每种咖啡饮料应列出其详细信息，如咖啡名称 [原料：水 50ml，牛奶 20ml，咖啡 30ml 等；热量：1.2 千卡] 和价格；菜单页面应设置退出选择；
2. 选择一种饮料后，机器应检查当前原料资源是否足够制作该饮料。如果不够，则打印引导信息给用户并返回菜单；否则继续；
3. 幸运数字游戏。询问消费者是否想参加幸运数字游戏；如果不想，则继续；如果想，要求消费者输入他/她的幸运数字（0-9 的整数），然后机器随机生成一个 0 到 1000 之间的整数，如果随机数的最后一位等于消费者的幸运数字，则执行 15% 的折扣；否则，引导消费者继续；
4. 优惠券状态检查。询问消费者是否有优惠券；如果有，引导消费者输入优惠券 ID 并检查其状态，并打印折扣详情；如果没有，引导消费者继续；
5. 接受现金。打印所有折扣后的饮料价格并引导消费者投入现金并自动计算总金额；接受的现金面值为 20 元、10 元、5 元和 1 元；
6. 处理现金。检查总金额是否足够购买该饮料；如果是，则询问消费者是否愿意将零钱捐赠给学校的公益活动，并引导消费者收取零钱；否则返回持续投入现金或退出交易；
7. 制作咖啡。打印咖啡制作步骤，例如准备、制作、包装；
8. 引导消费者取出饮料并返回欢迎菜单；
9. 机器应自动记录销售饮料并在交易完成后更新账户信息。




示例：
******************************************************************************* 
********************A nice day starts with a cup of coffee! ********************* 
*******************************************************************************
1. Cappuccino [Water: 50ml, Milk: 50ml, Coffee: 50ml; Heat: 1.2 kcal]: 12￥ 
2. Latte [Water: 80ml, Milk: 20ml, Coffee: 50ml; Heat: 1.0 kcal]: 10￥ 
3. Mocha [Water: 50ml, Milk: 50ml, Coffee: 40ml, Mocha: 10ml; Heat: 1.4 kcal]: 15￥ 
4. Cafe Americano [Water: 100ml, Milk: 0ml, Coffee: 50ml; Heat: 0.8 kcal]: 10￥ 
5. Espresso [Water: 70ml, Milk: 0ml, Coffee: 80ml; Heat: 1.3 kcal]: 14￥ 
Quit [Q/q] 
******************************************************************************* 
$ Please select your item: 3 
 
$ Your item is available, please enter ‘c’ to continue: c 
 
$ Do you want to attend the lucky number game? [y/n]: y 
 
$ Please input your lucky number (integer from 0-9): 6 
Congratulations! You win the game and luckily win a 15% discount! 
$ Is a coupon available? [y/n]: y 
 
$ Please input your coupon No.:  4312570 
You have a coupon with 15% discount! 
Your item price after discount is: 15*0.7 = 10.5 
$ Please enter your cash,  
$ how many 20￥count? : 0 
$ how many 10￥count? : 1 
$ how many 5￥count? : 0 
$ how many 1￥count? : 0 
Your total amount is: 10.0; Not enough money amount for buying! 
$ Please continue to insert your cash [c] or quit with [q]: c 
$ how many 20￥count? : 0 
$ how many 10￥count? : 0 
$ how many 5￥count? : 1 
$ how many 1￥count? : 0 
Your total amount is: 15.0; Your change is: 4.5 
$ Do you want to donate your loose change? [y/n]: y 
Your change is: 4.0, please receipt it!  
**Your coffee is making: 
------------------------------------------------------------------ 
** Coffee preparing finished! ------------------------------------------------------------------ 
** Coffee making finished! ------------------------------------------------------------------ 
** Coffee packaging finished! ------------------------------------------------------------------ 
$ Please take your coffee carefully! Press [R/r] to return the menu: r 
 
The items sold on this machine are: 
* Cappuccino: 0 
* Latte: 0 
* Mocha: 1  
* Cafe Americano: 0  
* Espresso: 0 
** Total profile: 10.5 