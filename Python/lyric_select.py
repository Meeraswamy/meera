#This is sample program

if_i_were_a_boy="""If I were a boy
Even just for a day
I'd roll out of bed in the morning
And throw on what I wanted and go

Drink beer with the guys
And chase after girls
I'd kick it with who I wanted
And I'd never get confronted for it
'Cause they'd stick up for me

If I were a boy
I think I could understand
How it feels to love a girl
I swear I'd be a better man
I'd listen to her
'Cause I know how it hurts
When you lose the one you wanted
'Cause he's taken you for granted
And everything you had got destroyed

If I were a boy
I would turn off my phone
Tell everyone it's broken
So they'd think that I was sleeping alone

I'd put myself first
And make the rules as I go
'Cause I know that she'd be faithful
Waiting for me to come home (to come home)"""

danse="""Oh my sweet torment,
No point in fighting, you start again
I’m just a worthless being
Without him I’m a bit troubled
I wander around alone on the subway
A last dance
To forget my great misery
I want to get away, everything to start again,
Oh my sweet torment

I stir the sky, the day, the night
I dance with the wind, the rain
A bit of love, a drop of honey
And I dance, dance, dance, dance, dance, dance
And in the noise, I run and I’m afraid
Is this my turn?
Here comes the pain
In all of Paris, I abandon myself
And away I fly, fly, fly, fly
Nothing but hope
On this road in your absence
Try as I might, without you my life is nothing but a meaningless shiny decor

I stir the sky, the day, the night
I dance with the wind, the rain
A bit of love, a drop of honey
And I dance, dance, dance, dance, dance, dance
And in the noise, I run and I’m afraid
Is this my turn?
Here comes the pain
In all of Paris, I abandon myself
And away I fly, fly, fly, fly"""

halo="""Remember those walls I built
Well, baby, they're tumbling down
And they didn't even put up a fight
They didn't even make a sound

I found a way to let you in
But I never really had a doubt
Standing in the light of your halo
I got my angel now

It's like I've been awakened
Every rule I had you breaking
It's the risk that I'm taking
I ain't never gonna shut you out

Everywhere I'm looking now
I'm surrounded by your embrace
Baby, I can see your halo
You know you're my saving grace

You're everything I need and more
It's written all over your face
Baby, I can feel your halo
Pray it won't fade away

I can feel your halo (halo) halo
I can see your halo (halo) halo
I can feel your halo (halo) halo
I can see your halo (halo) halo"""

birthday="""I heard you're feeling nothing's going right
Why don't you let me stop by
The clock is ticking, running out of time
So we should party, all night
So cover your eyes, I have a surprise
I hope you got a healthy appetite

If you wanna dance, if you want it all
You know that I'm the girl that you should call

Boy when you're with me
I'll give you a taste
Make it like your birthday everyday
I know you like it sweet
So you can have your cake
Give you something good to celebrate

So make a wish
I'll make it like your birthday everyday
I'll be your gift
Give you something good to celebrate

Pop your Perignon
We can get it on
So hot and heavy
Till dawn
I got you spinning
Like a disco ball
I'll have them playing
Your song

We're living the life
We're doing it right
You're never gonna be unsatisfied
If you wanna dance
If you want it all
You know I'm the girl that you should call

But when you're with me
I'll give you a taste
Make it like your birthday everyday
I know you like it sweet
So you can have your cake
Give you something good to celebrate

So make a wish
I'll make it like your birthday everyday
I'll be your gift
Give you something good to celebrate

Happy birthday"""

stay="""All along it was a fever
A cold sweat, hot headed believer
I threw my hands in the air, said, "Show me something"
He said, "If you dare, come a little closer"

Round and around and around and around we go
Oh, now tell me now, tell me now, tell me now you know

Not really sure how to feel about it
Something in the way you move
Makes me feel like I can't live without you
It takes me all the way
I want you to stay

It's not much of a life you're living
It's not just something you take, it's given

Round and around and around and around we go
Oh, now tell me now, tell me now, tell me now you know

Not really sure how to feel about it
Something in the way you move
Makes me feel like I can't live without you
It takes me all the way
And I want you to stay

Ooh, the reason I hold on
Ooh, 'cause I need this hole gone
Well, funny you're the broken one 
But I'm the only one who needed saving
'Cause when you never see the light 
It's hard to know which one of us is caving

Not really sure how to feel about it
Something in the way you move
Makes me feel like I can't live without you
It takes me all the way
I want you to stay
Stay
I want you to stay
Ooh"""

while True:
    print("Welcome, please select a select a song from this top 5 songs:\n")
    print("1 If I Were a Boy\n2 Dernière Danse\n3 Halo\n4 Birthday\n5 Stay")
    choice=int(input("Enter Number of Your Choice : "))

    if choice == 1:
        print("You chose If I Were a Boy. Here you go:")
        print(if_i_were_a_boy)
    elif choice == 2:
        print("You chose Dernière Danse. Here you go:")
        print(danse)
    elif choice == 3:
        print("You chose Halo. Here you go")
        print(halo)
    elif choice == 4:
        print("You chose Birthday. Here you go:")
        print(birthday)
    elif choice == 5:
        print("You chose Stay. Here you go")
        print(stay)
    end=input("Enter any key to quit or * to continue : ")
    if end == "*" :continue
    else:break
