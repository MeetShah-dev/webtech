import { Module } from '@nestjs/common';
import { AdminService } from './admin.service';
import { AdminController } from './admin.controller';
import { HttpModule } from '@nestjs/axios';
import { BlogController } from 'src/blog/blog.controller';
import { BlogService } from 'src/blog/blog.service';

@Module({
  imports: [HttpModule],
  providers: [AdminService],  // Ensure service is provided here
  controllers: [AdminController],
})
export class AdminModule {}
