import { Test, TestingModule } from '@nestjs/testing';
import { Oauth } from './oauth';

describe('Oauth', () => {
  let provider: Oauth;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      providers: [Oauth],
    }).compile();

    provider = module.get<Oauth>(Oauth);
  });

  it('should be defined', () => {
    expect(provider).toBeDefined();
  });
});
