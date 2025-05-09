import { Controller, Post, Body } from '@nestjs/common';
import { ClientProxyFactory, Transport, ClientProxy } from '@nestjs/microservices';

@Controller('order')
export class AppController {
  private client: ClientProxy;

  constructor() {
    this.client = ClientProxyFactory.create({
      transport: Transport.RMQ,
      options: {
        urls: ['amqp://localhost:5672'],
        queue: 'email_queue',
        // queueOptions: { durable: false },
        queueOptions: {
          durable: true,  // Make the queue durable
        },
      },
    });
  }

  @Post()
  async placeOrder(@Body() order: { email: string; product: string }) {
    // In a real app, you'd store order in DB here
    await this.client.emit('order_created', order);
    return { message: 'Order placed!' };
  }
}

// import { Controller, Get } from '@nestjs/common';
// import { AppService } from './app.service';

// @Controller()
// export class AppController {
//   constructor(private readonly appService: AppService) {}

//   @Get()
//   getHello(): string {
//     return this.appService.getHello();
//   }
// }
