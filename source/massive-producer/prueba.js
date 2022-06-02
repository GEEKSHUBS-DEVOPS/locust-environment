var kafka = require('kafka-node');

    const KeyedMessage = kafka.KeyedMessage;
    const Producer = kafka.Producer;
    const client = new kafka.KafkaClient({kafkaHost: '172.17.0.3:9092'});
    const producer = new Producer(client);

    km = new KeyedMessage('key', 'message');



    workbech = () => {    
        const payloads = [
            { topic: 'topic1', messages: 'hi', partition: 0 },
            { topic: 'topic2', messages: ['hello', 'world', km] },
            { topic: 'topic5', messages: ['number', Math.random(), km] },
        ];
        producer.send(payloads, function (err, data) {
            console.log(data);
        });
    };


    producer.on('ready', () => setInterval(workbech,1));
    
