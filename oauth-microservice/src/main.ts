import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import * as session from 'express-session';
import * as passport from 'passport';
const crypto = require('crypto');

const secretKey = crypto.randomBytes(64).toString('hex');
async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  app.enableCors({
    allowedHeaders: ['content-type'],
    origin: "http://localhost:3000",
    credentials: true
  })
  app.use(session({ secret: secretKey, saveUninitialized: false, resave: false, cookie: { maxAge: 60000, secure: false } }))

  app.use(passport.initialize())

  app.use(passport.session())
  await app.listen(3000);
}
bootstrap();
