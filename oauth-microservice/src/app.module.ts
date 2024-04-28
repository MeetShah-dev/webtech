import { MiddlewareConsumer, Module, RequestMethod } from '@nestjs/common';
import { AuthModule } from './auth/auth.module';
import { TypeOrmModule } from '@nestjs/typeorm';
import { User } from './user/entities/user.entity';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { AuthMiddleware } from './auth/auth.middleware';
import { RolesGuard } from './guards/role.guard';
import { APP_GUARD } from '@nestjs/core';
import { BlogModule } from './blog/blog.module';
@Module({
  imports: [
    TypeOrmModule.forRoot({
      type: 'postgres',
      host: process.env.DB_HOST,
      port: 5432,
      username: process.env.DB_USER,
      password: process.env.DB_PASSWORD,
      database: process.env.DB_DATABASE,
      synchronize: false,
      entities: [User],
      ssl: {
        rejectUnauthorized: false
      }
    }),
    AuthModule,
    BlogModule,
  ],
  controllers: [AppController],
  providers: [AppService, 
    {
    provide: APP_GUARD,
    useClass: RolesGuard,
  },
]
})
export class AppModule {
  configure(consumer: MiddlewareConsumer) {
    consumer.apply(AuthMiddleware)
    .exclude(
     { path: 'auth/google/login', method: RequestMethod.GET},
     { path: 'auth/google/redirect', method: RequestMethod.GET},
     { path: 'auth/status', method: RequestMethod.GET},
    )
    .forRoutes('*');
  }
}
