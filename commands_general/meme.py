import asyncio
import random

meme_list=['https://i.ytimg.com/vi/JII3ZDhp4CA/maxresdefault.jpg',
'https://i.pinimg.com/736x/62/bf/0d/62bf0d6b9ccd73f5e15aad8fa1d6163c.jpg',
'https://s3.india.com/wp-content/uploads/2019/02/valentines.jpg',
'https://img.delicious.com.au/WqbvXLhs/del/2016/06/more-the-merrier-31380-2.jpg',
'https://image.scoopwhoop.com/w960-h500-cfix/https://s4.scoopwhoop.com/anj/feat/941432013.jpg',
'https://perfectdaytoplay.com/wp-content/uploads/2020/05/Travel-funny-meme-covid19-pandemic-joke-humor-38.jpg',
'https://i.ytimg.com/vi/VrM-JkDnwiI/maxresdefault.jpg',
'https://i.ytimg.com/vi/zKxMTovmPN4/maxresdefault.jpg',
'https://i.imgur.com/k3pFRXd.jpg',
'https://starecat.com/content/wp-content/uploads/cats-and-dog-when-you-hold-your-hand-above-them-minecraft.jpg',
'https://i.pinimg.com/originals/1b/14/c3/1b14c30f94391830768d334f9234e412.jpg',
'https://i.pinimg.com/736x/a0/eb/34/a0eb3405be3afd0c622caf45b80fb4c7.jpg',
'https://static0.srcdn.com/wordpress/wp-content/uploads/2020/03/HarryPotterMemeHeader.jpg',
'https://images.indianexpress.com/2017/06/hp002_820.jp350'
'https://www.liveabout.com/thmb/__MZ-3UxWA5Y6Mvy545lYYbE/1265x800/filters:no_upscale():max_bytes(150000):strip_icc()/urawattharry-5ada2c3a18ba0100371a5552.JPG',
'https://i.pinimg.com/originals/6f/46/4f/6f464f022adadff6e831ecf54586a681.jpg',
'https://media.npr.org/assets/img/2015/03/03/overly_custom-39399d2cf8b6395770e3f10fd45b22ce39df70d4-s800-c85.jpg',
'https://cms.qz.com/wp-content/uploads/2018/07/meme-featured.jpg?qual75&stal41215',
'https://static.mommypoppins.com/styles/image620x420/s3/school_meme_3_0.jpg'
'https://s.yimg.com/ny/api/res/1.2/_twsNG4z4ENpWE7ZXoCJ2Q--/YXBwaWQ9aGlnaGxhbmRlcjt3PTk2MDtoPTk1OC4zNjE3NzQ3NDQwMjczO2NmPXdlYnA-/https://s.yimg.com/os/creatr-uploaded-images/2021-05/5d4f3960-acc5-11eb-bbff-5305b55ded14',
'https://i.imgflip.com/5c74jb.jpg',
'https://imgflip.com/i/5c74rc',
'https://imgflip.com/i/5c7539',
'https://imgflip.com/i/5c75bl',
'https://imgflip.com/i/5e5dk1',
'https://imgflip.com/i/5e5f1a']

async def meme_message(ctx):
  await ctx.send(random.choice(meme_list))
