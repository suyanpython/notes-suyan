import { Controller } from '@nestjs/common';
import { EventPattern, Payload } from '@nestjs/microservices';
import { Ctx, RmqContext } from '@nestjs/microservices'; // Import Ctx and RmqContext for RabbitMQ context

@Controller()
export class AppController {
  @EventPattern('order_created')
  async handleOrderCreated(
    @Payload() data: any,
    @Ctx() context: RmqContext, // Use @Ctx() and the specific context type (e.g., RmqContext for RabbitMQ)
  ) {
    console.log(`📨 Received message to send email:`, data);

    // Simulate a delay or some business logic
    setTimeout(() => {
      console.log(`📨 Sending email to ${data.email} about product ${data.product}`);

      // After processing, acknowledge the message manually.
      context.getChannelRef().ack(context.getMessage()); // Manually acknowledge the message
    }, 5000); // Simulate some delay
  }
}