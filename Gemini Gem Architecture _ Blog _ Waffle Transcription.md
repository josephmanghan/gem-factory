So, I am a software developer. And I've been getting really into AI engineering and genetic development, and I'm basically kind of rightly building that you talked earlier around some of these skills. Apparently, my place is more in the kind of. Um, stlc, side of things where I am. Things me about more kind of native genetic Solutions.

For sort of like, you know, code writing and that sort of thing. I am gradually moving towards, um. Ai engineering, um, anyway, that's the problem. Um. And what I'm sort of like talking about at the moment is, um. I've actually did that. A lot of experience with making Gemini gems and?

On the one hand, the kind of solutions you can produce with gems. You know, you could argue, are like more low-tech and less powerful than other, more like proprietary Solutions? But I think there is a case to be made for using jets. And. I want to talk a little bit about that a little bit about my approaches.

So? I think two key things to highlight with us, maybe a few things actually. Number one is. Gemini 3\. Is really powerful. It is a marked difference over 2.5. Personally, I do, I mean. Within the IDE. The Improvement has been impressive enough to warrant me. And, you know, moving away from using Claude as my main?

Model. But at the same time. I think there's probably a little bit of tinkering to do. It's for it to improve, like, actual, like integrated coding tasks, because I suspect it's a potential is quite high, and that certainly seems to be the case from some of the tests that.

Are being put to on the model, but as far as like, reasoning is concerned. And it's and and its aptitude for processing. Wow, it is very beautiful. Some other things to talk about with regard to gems would be the contact window. Um Gemini in the web UI. Has access to.

Million token context window? And that is. Um, very, very sizable. In the IDE, it's something like 200, 000\. Um, which you can run out of very, very quickly. You provide a lot of context in the IDE and. You gotta run out of conflict very quickly, so you need to navigate.

Uh, contact management strategies. Which? Is doable, but can be. A point of friction, but also can actually, at times, kind of potential. Um, for kind of workflows. And uh, not all web uis are weak on this sense. Generally speaking at web, UI probably has a bit more complex, but for instance, Claude AI quite limited context with no, frankly.

Um. And uh, in in the web UI. Uh, and then none of them actually, even Gemini. You don't get any representation of how close you are to completing. Uh, the context windows. That'd be a bit annoying, so the fact that it's very large in Gemini is. Um. A good thing because it means you run likely to reach the end of it.

The context window in Gemini web UI is such that you can provide. A really extraordinary amount of data. As sort of like a gem setup. Um, which granted is obviously something that could be done with. You know, a vector-based? Rag set up with a bit of agent or frustration.

But it's just natively inbuilt to Gemini that it can handle. Um, large amount of second staff that data, as well as a long conversation and the fact that it is so accessible, is my third point, it's a very, very accessible tool. All you need to do is share. But yeah, because that's another new feature that's been introduced recently.

You just needs a share, and you people can just get involved. There are also some other really great aspects of gens to talk about. One is the fact that gems can receive updates. So, if you are someone that is managing, you can someone can manage a gen.

I'm basically. You can attach from any Google Suite file. Upload those knowledge files to the gym, so let's say you have instructions about how the job should operates, or you have a data files that you know the kind of like a knowledge base for the gem? If you would have to provide Google Drive?

Then the GM is going to get those updates for free, so you don't need to tell a user. Oh, please get the new gem. Here's the new link. They just get it for free. Now, that's not strictly the same with. Like, for the kind of system prompts that houses the whole thing.

That, even within that space, there's some degree is kind of flexibility, because actually, you can update. That excuse construction without them, um? For that. That needs to update, but we also can do with the knowledge files is basically. If you've got multiple gems that access the same tiles, and we all get into three so you can have sort of instances of the GM that are perhaps defined in slightly different ways.

It's all shared, so that's absolutely. It is my belief that there are some genuine use cases for James, and I know that the custom tbc's out there. And I know that there's a lot of strength in that Marketplace and in tbc5, but certainly I think that the raw power and the context?

Uh. Virus virus for sure. What is asking them now? I also want to talk a little bit about, um, more important, because that was just the context really. I want to talk about the architecture tonight being utilizing. Now, this is like a. Um, point of refinement. For me, that's something I've explored a lot, but um.

I've been kind of developing a architecture. That allows for a degree of atomization. Um, allows for. The deployment in this way that I talked about, which is where you have these Google Drive uploads, so it can then. Also, what's open in the gem and also cases for performance because?

In theory, you get 10 Max files, right? You can upload noise. They can be as long as you like if you get 10 Max files. So, something like a hexagonal architecture? It's never going to work. You certainly can start thinking about that kind of complexity for a gem. But uh, if you have too many files.

Then, and you just you're talking about to fill the space. And then the other sort of issue with optimization is as much as. Gemini, especially Gemini, especially Gemini 3 as much as it can. Process. Really incredible. Um. Sort of bed of files and such as graphic context more equals.

Um. Performance hit, right? So, for instance, I've been maintaining a refinement gem at work, and this refinement gem has two workflows within it, as well as like a helper workflow commands, you might think of it as and what this does. The first one is about taking an idea from a sort of.

Open state what we might throw to in in agile is like an open ticket, which basically is just a header to draft. So it's kind of throughout information. The basic premise, no technical details, products information. Then there's the second workflow. That takes it from. Draw to a sort of ready for Dev, ready for refinement type of state.

I've like, I said, I've refined an architecture selector and a large amount of complexity and reasoning and elicitation and steps. Um, step by step wise elicitation process can be delivered. But even with those refinements, if I have a gem with both of those workflows, we're talking about a five to ten second hit per front for the agency process.

Unfortunately, does not appear to be. Um. Uh, have any kind of clever rag level retrieval, um? Uh, simply those files exist in those files processed, so you do need to be careful if you're worried about performance with. Uh, not overloading information, but anyway. What also is the case is a limit?

Is it not just the limiters you've been careful? Spirit wasn't selection network files. Um, it's slightly better. Retrievers equals performance hit from my experience.

So, I've developed an architecture which I think is. Uh, proven to be very, very effective. I've been very impressed. It balances atomization, and there's more maintainability and and the capacity for iteration with performance. Um, and I just want to tell you a little bit about it so. The it's got a few kind of four tenants, and essentially it's kind of.

Explain architecture risk approach. I would say, um, we start with the Asian definition. And this is what goes into the system instruction. Which is the kind of the core sort of description? Um, that when you edit the gem, you break. A gem just goes into the main pane there, and I can provide an image here.

This Asian definition is in a yaml format. It is written entirely in general. Heavily relies upon.

Uh, a, a conservative token usage. And explicitly clear instructions through a high, high signal, slow noise. Um, construction, and it basically denotes the key tenants. Off the agent, so it's got in it its name. Uh, it's got in it. The kind of high level principles, and then it adheres to critical requirements and constraints, and then it lists its dependencies with labels.

So, it makes it explicitly clear all the knowledge files. Uh. What they represent, and then the most important thing is, I list commands. I provide an example of this. So, one of the key tenets of? Ah, the gem is the ability of my architectures. Whoever this is called commands.

Now, these commands are linked to specific instructions files that I'll get to in a moment, but essentially, the what is working exceeding well because it is the aging definition you can write to. The command exists and say. Um, begin stage one refinement. You can link that. To a specific instructions file.

Hold stage one refinement. And when the user? Types over slash. Stage on refinement. It will begin that workflow and without. Any complicated? Uh, triggering architectures deterministic, triggering art architectures. That workflow is the gun I've got to say. It's very, very impressive how well the reasoning effort manages to pass this.

Uh, and I can get a little bit more into that in a moment as well, because there's some other cool things you can do. Um, I do have to say first, uh, for Courtney first, though. So, that's a lot of a lot of the sort of, um, my inspiration comes from the bmas methodology.

It's really important that I shout, um, that out? Um, they have a slightly different use case. A slightly more focused view and a slightly broader kind of utility. And then what I'm talking about. Um, but? Many of my ideas come from that, and it's very impressive spectrum development, um.

Uh, workflow. That should absolutely be checked out, but yes. Anyway, we start with that agent definition. And then. Some important things to come with it. So, like I said, we have these commands, right? And those commands left with this. Uh, speak to specific Instructions files, and those are writers help.instructions.md or gdoc stage one refinement instructions.MD, so they next to the command definitions, the actual file type, and it knows to Simply call it.

Um.

And so basically, what we have is. An XML. What we have is a markdown tile. Um, that's a note in a sort of in a kind of imperative. Uh, sequence the instructions, but how something should take place? Um, I do find that an imperative approach. For give it like a script.

It's something that works a little bit better than a decorative approach. Here, I have tried. Uh, a definitely of approach. In the past, where we kind of, um, denote States for a specific file that are called upon to instantiate the file. That is not something I found to be particularly effective yet in Gemini.

I think that the sort of. Imperative sequential. Um, step-wise, kind of architecture or something that seems to be working a little bit better. And there's a lot more reliable. So we have our instructions anyway. Essentially, it's just a markdown page, but very careful token usage. And, um. Very um, imperative in style.

The other thing, um? I want to say is again on the token usage. Way to reduce the amount of tokens is a good thing. I actually have experimented with the caveman style language. I do find. That sometimes, um. That leads into the way Gemini talks. So that's something I'm still tinkering with.

Um. For instance, if we remove all stopgap words from an instructions file, sometimes that's leaking into how the agent talks to the user. Um, because it's, I think I think it sort of picked it up as its personality, so definitely something to explore there, because any reduction in token usage is a good for the long term state of an ongoing conversation, but is also good for performance.

Um, but just something to think about there, um? Now, one thing that the whilst, maybe a declarative, uh, sort of architecture, is something that hasn't worked too. Well, that's not to say, there aren't great opportunities. For code-like reasoning. So certainly. All agents are really good at interpreting pseudo code, where we can say, you know, if this, do this, and you, you pack up.

Um, arguments together that. Um. Create sort of states and things like that. I do find that in the if you have a particularly large gem. That again. Whilst it's not always declarative. Having? A deep logic like that doesn't work too well, um, more, to be explored, but I think.

Any kind of logic just needs to be handled from one central location, which is the agent definition, and from there that calls needs to be called, and it gets run. Um. That's not to say that there aren't opportunities for kind of abstraction and for code, like logic, and one way I do this that I find is really effective is you can use variables now at the end of the day.

It's not like there are any particular. Syntax that are appropriate and the agent's able to reason quite a bit. But I do this where I have. And open and close curly brackets. And then I have in cats lock using. Uh, underscore case, um, variable name. So, for instance, in my refinement gem.

At the end of each solicitations yet. I have output answer to, for example, description. And then I have another file. That's called templates, and this template denotes the template for the ultimate ticket that is refined and basically the agent knows to hold in its memory. That's that variable. And when it comes to make the table, the the template to utilize it to create the refine ticket, it can stick that answer in there, and that's just absolutely amazing ability to get some reliability out of the final output.

And of course, you can kind of use that variable kind of logic in a variety of other ways as well. So that's I think a very cool thing to think about. And speaking of this template, that's the kind of next days, really, because? We start this definition, but below it.

We have almost like this sort of a business logic level. It's a combination of business logic and UI, but beneath that we can have any number of things, right? So, I often use templates to denote the exact output of a workflow I've already described that. You can use a knowledge base.

Google sheet is absolutely incredible for this because you can be actually be quite. Curated with? The information became maintained within a knowledge base because you can use different sheets and all of those sheets can be. Uh, obviously uploaded to the gem on the association. So, there's a lot of opportunity for optimization in there, of course.

More information equals performance here, and everything like that, but we're using them regularly just to add knowledge base, and it proves very, very effective. You always need very clear labeling with all information like this. We have to pretend that it's a vector kind of structure where there are always.

You know keys and values? Um, items and descriptions. So that the agent knows how to pull information. And that can add some syntactic complexity, but it's absolutely doable. So, we have templates. We have data in this form of knowledge base. And really days. You can take any form then, and you can always refer to that data in the same kind of logic variable based way.

So, all in all, I think, created some really powerful gems. I'm happy to share them. We have this refinement, Jim. We've also got a user testing gem where we have about 20 users. All with explicit, and while refined varies, personalities. And.

Uh, they can be used to sort of enter, like a party mode, where they can talk together because of product. One idea or a website or anything like that? Uh, ux design. It's, and it's so impressive. And yes, you know. There are going to be other identity tools out there right now, but this.

Is free. It is really powerful. Um. And. It's, it's really, really accessible, and you can get hold of this something I've been talking a lot at. Work recently about is wanting to exist in the shed ecosystems, all the roles. Well, we're starting to. And move into territories. Because of this sort of a genetic Revolution where the boundaries between roles.

Are really blurring that. There Still Remains sort of an expertise, then individually speaking. I think with that comes a really strong capacity for us all to start living within the same ecosystem, whether we're devs, whether we're product owners. Uh, whether we're ux. And by being in a shared ecosystem that really elicits the capacity for parity for productivity.

As well as I'm really unlocking like? An agenda capacity, because, um, we have everything all specs exist and are easily retrieved in the right space. And ideally, I think that place is going to be the IDE, but where something like floor code and an exceptional map skills helps capture them all in the same place, but for us all, insisting in Gemini and bringing that parity there.

That's definitely a step in the right direction, and I think that's pretty cool. So, I think in terms of if I was speak to speak to takeaways it was, it would simply be. You know, guess in, try getting into gems. They're so accessible, and I think that there's going to be a lot more to come in this space.

Um, it's only been recently where they've actually allowed the ability to share these things, and I can see a Marketplace coming in the future. And that's not to mention that currently. We're still on 2.5 flash when three flash comes out. I think that's going to be a really incredible for each as well.

I do use 2.5 flash for some specific gems where I don't need deep reasoning, but if the level of reasoning for Flash and that the speed is incredible on flashlight, it's the reason it can go up. Wow, that's going to be an incredible use case. Um, so try gems.

Try my architecture. Um. And what I can also do here is I can provide my architecture. As like a system introduction. Um, so like I can just like you have a promise. It's like this is the session setup for what I think in architecture would be use it to create another gen.

I think that'd be a really great thing to, uh, to put together. Um, I could even like, oh, I should definitely put that into into GitHub as an example. Oh, I should definitely do that. Okay, there we go.

You can also use code2promp to convert into a web bundle

Unfortunately, whilst you can write in .docx in the IDE and frictionlessly upload that to Google Doc, a drag and drop file replace breaks the gem. Personally I think it’s better to write in markdown and then copy and paste from markdown within a maintained file.   
I use a deploy script that builds to dist by processing out stopgap words to reduce token count (skipping essential files like agent definition and [help.instructions.md](http://help.instructions.md) which is often copy and pasted by the agent), and then processes a web bundle that can be used as a quick start into using the gem without needing to make a gem

An easy way to deploy INITIALLY is by dragging the md files into drive, clicking on them and rendering as doc then deleting the md files. Maintain these forever now. I also convert all yaml to md at the end so same can be done with these. Do NOT do this for CSV as Gemini gets very confused. Make a fresh sheet and import.