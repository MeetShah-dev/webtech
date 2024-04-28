// blog.module.ts
import { Module } from '@nestjs/common';
import { HttpModule } from '@nestjs/axios';
import { BlogService } from './blog.service';
import { BlogController } from './blog.controller';

@Module({
  imports: [HttpModule],
  providers: [BlogService],  // Ensure service is provided here
  controllers: [BlogController],
})
export class BlogModule {}
