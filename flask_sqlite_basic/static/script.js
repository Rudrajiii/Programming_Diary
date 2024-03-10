console.log("plugged up done!");
const text = new SplitType("h1");
gsap.from('.char',{
    y:-100,
    stagger:0.05,
    duration:0.5,
});
gsap.from('.apps',{
    x:-1000,
    opacity:0,
    stagger:0.3,
    duration:0.4,
});
gsap.from('.image',{
    scale:0,
    opacity:0,
    duration:1.1
})
