function diceStreakGamble(player1,player2,player3,player4){
    const scores = [
        consecutiveWalk(player1),
        consecutiveWalk(player2),
        consecutiveWalk(player3),
        consecutiveWalk(player4)
    ];

    let maxScore = scores[0].length;
    let index = 0;

    for(let i = 0; i < scores.length; i++) {
        if(maxScore < scores[i].length) {
            maxScore = scores[i].length;
            index = i;
        }
    }

    return `Winner: Player ${index+1} won $${maxScore * 4} by rolling [${scores[index]}]`; 
}

function consecutiveWalk (arr) {
    stack = [];
    stack.push(arr[0]);

    for(let i = 1; i < arr.length; i++) {
        if (stack[stack.length - 1] > arr[i]) {
            let max = 0;
            while (stack.pop() != undefined);
        }
        stack.push(arr[i]);
    }

    return stack;
}